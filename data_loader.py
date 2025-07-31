from pathlib import Path
import pandas as pd

def load_stations():
    base_path = Path(__file__).parent / "data" / "as_is"
    df1 = pd.read_csv(base_path / "df_trento.csv")
    df2 = pd.read_csv(base_path / "df_crema.csv")
    
    df = pd.concat([df1, df2], ignore_index=True)
    df = df.rename(columns={"Latitude": "lat", "Longitude": "lon", "Title": "title"})
    df = df[["lat", "lon", "title", "charging_station_type", "PowerKW"]].dropna()
    
    return df.to_dict(orient="records")