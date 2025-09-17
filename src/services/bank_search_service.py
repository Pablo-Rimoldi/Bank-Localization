from typing import Dict, Any, List

import requests

from src.models.bank_result import BankResult
from src.utils.config import settings


class BankSearchService:
    TARGET_CATEGORIES = [
        "bank",
        "post_office",
    ]

    def search(self, isoline_geojson: Dict[str, Any]) -> List[BankResult]:
        # Using Geoapify places within polygon via filter=place: Supports circle; for polygon one may pre-filter by bbox and post-filter by point-in-polygon.
        # Here we keep a simple stub to be implemented according to chosen provider limits.
        _ = isoline_geojson
        # Placeholder: return empty list; real implementation will call provider and map to BankResult
        return []


