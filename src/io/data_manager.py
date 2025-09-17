from typing import List
import pandas as pd
from src.models.debtor_record import DebtorRecord
from src.models.bank_result import BankResult


INPUT_REQUIRED_COLUMNS = ["codice_fiscale", "indirizzo_residenza"]


class DataManager:
    def read_debtors(self, input_csv_path: str) -> List[DebtorRecord]:
        df = pd.read_csv(input_csv_path)
        for c in INPUT_REQUIRED_COLUMNS:
            if c not in df.columns:
                raise ValueError(f"Colonna mancante: {c}")

        records: List[DebtorRecord] = []
        for _, row in df.iterrows():
            records.append(
                DebtorRecord(
                    codice_fiscale=str(row.get("codice_fiscale", "")).strip(),
                    indirizzo_residenza=str(row.get("indirizzo_residenza", "")).strip(),
                    eta=int(row["eta"]) if "eta" in df.columns and pd.notna(row.get("eta")) else None,
                    mobilita_ridotta=bool(row["mobilita_ridotta"]) if "mobilita_ridotta" in df.columns and pd.notna(row.get("mobilita_ridotta")) else None,
                )
            )
        return records

    def write_results(self, output_csv_path: str, rows: List[dict]) -> None:
        df = pd.DataFrame(rows)
        df.to_csv(output_csv_path, index=False)

    @staticmethod
    def build_output_row(debtor: DebtorRecord, banks: List[BankResult]) -> dict:
        row = {
            "codice_fiscale": debtor.codice_fiscale,
            "indirizzo_residenza": debtor.indirizzo_residenza,
        }
        for idx in range(5):
            prefix = f"banca_{idx+1}_"
            if idx < len(banks):
                b = banks[idx]
                row[prefix + "nome"] = b.nome
                row[prefix + "indirizzo"] = b.indirizzo
                row[prefix + "tempo_min"] = b.tempo_min if b.tempo_min is not None else ""
                row[prefix + "trasporto"] = b.trasporto if b.trasporto is not None else ""
            else:
                row[prefix + "nome"] = ""
                row[prefix + "indirizzo"] = ""
                row[prefix + "tempo_min"] = ""
                row[prefix + "trasporto"] = ""
        return row


