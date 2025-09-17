from dataclasses import dataclass
from typing import Optional


@dataclass
class DebtorRecord:
    codice_fiscale: str
    indirizzo_residenza: str
    eta: Optional[int] = None
    mobilita_ridotta: Optional[bool] = None


