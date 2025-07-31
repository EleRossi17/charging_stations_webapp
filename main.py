from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.responses import JSONResponse
import pandas as pd
import os
from data_loader import load_stations

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index():
    return Path("static/index.html").read_text()

@app.get("/stations")
def stations():
    return load_stations()

@app.get("/api/stations")
def get_stations():
    path = "data/as_is"
    dfs = []
    for file in os.listdir(path):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(path, file))
            dfs.append(df)
    merged_df = pd.concat(dfs)
    return JSONResponse(content=merged_df.to_dict(orient="records"))