from dataclasses import dataclass
from typing import Optional


@dataclass
class BankResult:
    nome: str
    indirizzo: str
    tempo_min: Optional[int]
    trasporto: Optional[str]
    priority_score: Optional[float] = None
    gruppo: Optional[str] = None


