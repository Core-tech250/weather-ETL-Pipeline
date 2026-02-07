from src.extract import fetch_weather
from src.transform import transform_weather
from src.load import init_db, load_data
from src.logger import logger

def run_pipeline():
    try:
        logger.info("Pipeline started")

        raw = fetch_weather()
        logger.info("Data extracted")

        df = transform_weather(raw)
        logger.info("Data transformed")

        init_db()
        load_data(df)
        logger.info("Data loaded into database")

        logger.info("Pipeline finished successfully")

    except Exception as e:
        logger.error(f"Pipeline failed: {e}")
        raise
