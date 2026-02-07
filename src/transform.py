import pandas as pd
from datetime import datetime
from config import CITY

def transform_weather(raw_json):
    """Convert API JSON into structured dataframe"""

    weather = raw_json["current_weather"]

    df = pd.DataFrame([{
        "city": CITY,
        "time_utc": pd.to_datetime(weather["time"]),
        "temperature_c": weather["temperature"],
        "wind_speed_kmh": weather["windspeed"],
        "wind_direction": weather["winddirection"],
        "source": "api",
        "ingestion_time": datetime.utcnow()
    }])

    return df
