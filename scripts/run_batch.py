import sys

from src.bank_proximity_system import BankProximitySystem
from src.utils.logging_setup import setup_logging


def main() -> None:
    if len(sys.argv) < 3:
        print("Uso: python scripts/run_batch.py <input_csv> <output_csv>")
        sys.exit(1)
    setup_logging()
    input_csv = sys.argv[1]
    output_csv = sys.argv[2]
    system = BankProximitySystem()
    system.process_batch(input_csv, output_csv)


if __name__ == "__main__":
    main()
