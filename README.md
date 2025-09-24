## Sistema Localizzazione Banche

Struttura base del progetto per il sistema di localizzazione banche e generazione output CSV secondo le specifiche fornite.

### Avvio rapido
- Creare un file `.env` copiando `.env.example` e compilare le chiavi API.
- Installare le dipendenze: `pip install -r requirements.txt`
- Eseguire un test locale con dati di esempio: `python scripts/run_batch.py data/debitori_input.csv data/banche_prossimita_output.csv`

### Struttura cartelle (semplificata)
- `src/bank_proximity_system.py`: orchestratore principale
- `src/data_manager.py`: I/O CSV
- `src/models`: modelli dati (`DebtorRecord`, `BankResult`, `Enums`)
- `src/services`: servizi (geocoding, isolinee, ricerca banche, ranker, trasporti)
- `src/utils`: config e logging
- `scripts`: esecuzione singola e batch
- `data`: CSV di input/output di esempio
- `tests`: test di base

### Specifiche I/O
- Input richiesto: `debitori_input.csv` con colonne `codice_fiscale, indirizzo_residenza` e opzionali `eta, mobilita_ridotta`.
- Output: `banche_prossimita_output.csv` con 5 risultati massimo per debitore.


