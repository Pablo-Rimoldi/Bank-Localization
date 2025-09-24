from typing import List
from src.models.debtor_record import DebtorRecord
from src.models.enums import AreaType
from src.models.bank_result import BankResult
from src.services.geolocation_service import GeolocationService
from src.services.transport_optimizer import TransportOptimizer
from src.services.isoline_service import IsolineService
from src.services.bank_search_service import BankSearchService
from src.services.bank_ranker import BankRanker
from src.data_manager import DataManager


class BankProximitySystem:
    def __init__(self) -> None:
        self.geo = GeolocationService()
        self.transport = TransportOptimizer()
        self.isoline = IsolineService()
        self.search = BankSearchService()
        self.ranker = BankRanker()
        self.io = DataManager()

    def process_debtor(self, debtor: DebtorRecord) -> List[BankResult]:
        coords = self.geo.geocode(debtor.indirizzo_residenza)
        if not coords:
            return []
        lat, lon = coords

        # Context detection (placeholder: unknown density/elevation → defaults per rules)
        area = AreaType.URBAN  # A simple default; refine when density/elevation available

        mode = self.transport.select_mode(
            area, debtor.eta, debtor.mobilita_ridotta)
        minutes = self.isoline.compute_minutes_by_context(area.value)
        polygon = self.isoline.build_isoline(lat, lon, minutes, mode)
        banks = self.search.search(polygon)

        # order and limit
        ranked = self.ranker.rank_and_limit(banks, max_per_group=2, limit=5)
        # attach transport mode where missing
        for b in ranked:
            if not b.trasporto:
                b.trasporto = mode.value
        return ranked

    def process_batch(self, input_csv_path: str, output_csv_path: str) -> None:
        debtors = self.io.read_debtors(input_csv_path)
        rows: List[dict] = []
        for d in debtors:
            banks = self.process_debtor(d)
            rows.append(self.io.build_output_row(d, banks))
        self.io.write_results(output_csv_path, rows)
