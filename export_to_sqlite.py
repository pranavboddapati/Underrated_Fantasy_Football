import pandas as pd
import mysql.connector
import sqlite3

# Step 1: Read from MySQL
conn_mysql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DataScience",
    database="fantasy"
)

df = pd.read_sql("SELECT * FROM fantasy_2024_stats", conn_mysql)
conn_mysql.close()

# Step 2: Export to SQLite
conn_sqlite = sqlite3.connect("fantasy.db")
df.to_sql("fantasy_2024_stats", conn_sqlite, if_exists="replace", index=False)
conn_sqlite.close()

print("✅ Exported to fantasy.db (SQLite)")
