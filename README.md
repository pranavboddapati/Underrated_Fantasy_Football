# Underrated Fantasy Football Model (2025)

This project predicts the most underrated fantasy football players by position using performance stats and previous year's ADP

## Features
- Pulls ADP data from API
- Feature engineering based on position-specific stats
- Predicts upcoming ADP
- Calculates "underrated score"

## Files
- `underrated_model.ipynb`: Full model with feature engineering
- `fantasy.db`: SQLite database with cleaned player statistical data
- `create_fantasydb.py`: Code to create database
- `import_fantasydata_to_mysql.py`: code to import data into table in database
- `export_to_sqlite.py`: Code to create .db file
- `fantasy_data.csv` - csv containing player statistics

## Usage
Run the Colab notebook or execute Python scripts to preprocess and analyze data.

