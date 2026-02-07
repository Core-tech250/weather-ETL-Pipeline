import sqlite3
from config import DB_PATH

def init_db():
    """Create table if it does not exist"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        time_utc TIMESTAMP,
        temperature_c REAL,
        wind_speed_kmh REAL,
        wind_direction REAL,
        source TEXT,
        ingestion_time TIMESTAMP,
        UNIQUE(city, time_utc)
    );
    """)

    conn.commit()
    conn.close()


def load_data(df):
    conn = sqlite3.connect(DB_PATH)
    try:
        df.to_sql("weather_data", conn, if_exists="append", index=False)
    except Exception:
        print("Duplicate record ignored")
    finally:
        conn.close()
