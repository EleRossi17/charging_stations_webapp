# EV Charging Stations WebApp

Applicazione web per visualizzare stazioni di ricarica elettrica su mappa interattiva.

## Funzionalità attualmente presenti

- Visualizzazione dei punti di ricarica da due dataset CSV (`df_trento.csv`, `df_crema.csv`)
- Backend FastAPI con endpoint `/stations`
- Frontend HTML statico con Leaflet.js
- Marker interattivi con informazioni su titolo, tipo e potenza

## Struttura

├── main.py
├── data_loader.py
├── df_trento.csv
├── df_crema.csv
├── static/
│ └── index.html
├── requirements.txt
└── README.md


## Requisiti

- Python 3.8+
- pacchetti: `fastapi`, `uvicorn`, `pandas`

## Setup e avvio

### 1. Installazione pacchetti (globale o venv)

```bash
pip install -r requirements.txt
```

### 2. Avvio
```bash
python uvicorn main:app --reload
```