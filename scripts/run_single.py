import sys

from src.core.bank_proximity_system import BankProximitySystem
from src.models.debtor_record import DebtorRecord
from src.utils.logging_setup import setup_logging


def main() -> None:
    if len(sys.argv) < 3:
        print("Uso: python scripts/run_single.py <codice_fiscale> <indirizzo_residenza>")
        sys.exit(1)
    setup_logging()
    codice_fiscale = sys.argv[1]
    indirizzo = " ".join(sys.argv[2:])
    system = BankProximitySystem()
    debtor = DebtorRecord(codice_fiscale=codice_fiscale, indirizzo_residenza=indirizzo)
    banks = system.process_debtor(debtor)
    for b in banks:
        print(f"{b.nome} | {b.indirizzo} | {b.tempo_min} | {b.trasporto}")


if __name__ == "__main__":
    main()


