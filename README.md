# Cyberpills

Raccolta di piccoli progetti di cybersecurity/scripting in Python. Pensata come sandbox personale per sperimentare strumenti di base (scansione porte, gestione password, ecc.).

## Struttura

- `port-scanner/` – scanner di porte che usa `nmap` via il wrapper Python `python-nmap`.
- `password-manager/`
  - `passgen.py` – genera password casuali.
  - `passman.py` – demo minimale di password manager in memoria (hash SHA-256, niente salvataggio su disco).

## Prerequisiti

- Python 3.x
- CLI di Nmap installata e nel `PATH` (es. `brew install nmap` su macOS, `sudo apt install nmap` su Debian/Ubuntu).
- Dipendenze Python: `python -m pip install python-nmap` (serve per `port-scanner`).

Per isolare il tutto:

```bash
python -m venv .venv
source .venv/bin/activate
pip install python-nmap
```

## Uso rapido

### Port scanner

1. Apri `port-scanner/portscanner.py` e imposta `target` (IP/hostname da scansionare).
2. Esegui:

```bash
python port-scanner/portscanner.py
```

Nota: scansiona solo host che possiedi o per cui hai autorizzazione.

### Password generator

```bash
python password-manager/passgen.py
```

### Password manager (demo)

```bash
python password-manager/passman.py
```

Consente di creare utenti e fare login nella stessa sessione (i dati non vengono salvati su file).

## Aggiungere nuovi progetti

Metti ogni esperimento in una nuova cartella con uno script principale e una breve nota su requisiti/uso. Mantieni il focus su esercizi didattici e legali.
