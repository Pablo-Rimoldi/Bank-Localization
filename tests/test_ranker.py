from src.services.bank_ranker import BankRanker
from src.models.bank_result import BankResult


def test_ranker_orders_by_score_and_limits_group():
    r = BankRanker()
    results = [
        BankResult(nome="Unicredit Banca", indirizzo="A",
                   tempo_min=20, trasporto="walk"),
        BankResult(nome="Intesa Sanpaolo", indirizzo="B",
                   tempo_min=15, trasporto="walk"),
        BankResult(nome="Poste Italiane", indirizzo="C",
                   tempo_min=10, trasporto="walk"),
        BankResult(nome="BCC Milano", indirizzo="D",
                   tempo_min=8, trasporto="walk"),
        BankResult(nome="Banco BPM", indirizzo="E",
                   tempo_min=12, trasporto="walk"),
        BankResult(nome="Unicredit Filiale 2", indirizzo="F",
                   tempo_min=25, trasporto="walk"),
        BankResult(nome="Unicredit Filiale 3", indirizzo="G",
                   tempo_min=5, trasporto="walk"),
    ]
    ranked = r.rank_and_limit(results, max_per_group=2, limit=5)
    assert len(ranked) == 5
    # Ensure no more than 2 Unicredit
    assert sum(1 for x in ranked if (
        x.gruppo or "").startswith("UNICREDIT")) <= 2
