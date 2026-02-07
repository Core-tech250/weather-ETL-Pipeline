# weather-ETL-Pipeline
A modular ETL pipeline that fetches real-time weather data from an API, transforms it into a structured schema, and loads it into a SQLite database with duplicate protection and logging.
#Features
.)Extracts live weather data from Open-Meteo API
.)Transforms raw JSON into structured tabular format
.)Loads data into relational database
.)Prevents duplicate records using unique constraints
.)Maintains historical data
.)Logs pipeline execution
