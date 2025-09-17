from typing import List, Dict

from src.models.bank_result import BankResult


BANK_WEIGHTS: Dict[str, int] = {
    "UNICREDIT": 10,
    "INTESA SANPAOLO": 9,
    "POSTE": 8,
    "BANCOPOSTA": 8,
    "BCC": 7,
    "BPM": 6,
    "BPER": 5,
    "MEDIOLANUM": 4,
    "MONTE DEI PASCHI": 3,
}


def _infer_group(name: str) -> str:
    upper = name.upper()
    for key in [
        "UNICREDIT",
        "INTESA SANPAOLO",
        "POSTE",
        "BANCOPOSTA",
        "BCC",
        "BPM",
        "BPER",
        "MEDIOLANUM",
        "MONTE DEI PASCHI",
    ]:
        if key in upper:
            return key
    return "ALTRE"


class BankRanker:
    def score(self, result: BankResult) -> float:
        group = result.gruppo or _infer_group(result.nome)
        weight = BANK_WEIGHTS.get(group, 1)
        tempo = result.tempo_min or 9999
        return (weight * 100) - tempo

    def rank_and_limit(self, results: List[BankResult], max_per_group: int = 2, limit: int = 5) -> List[BankResult]:
        # compute scores
        for r in results:
            r.gruppo = r.gruppo or _infer_group(r.nome)
            r.priority_score = self.score(r)

        # sort desc
        sorted_results = sorted(results, key=lambda r: (r.priority_score or -1), reverse=True)

        # enforce max per group and limit
        group_counts: Dict[str, int] = {}
        final: List[BankResult] = []
        for r in sorted_results:
            grp = r.gruppo or "ALTRE"
            if group_counts.get(grp, 0) >= max_per_group:
                continue
            final.append(r)
            group_counts[grp] = group_counts.get(grp, 0) + 1
            if len(final) >= limit:
                break
        return final


