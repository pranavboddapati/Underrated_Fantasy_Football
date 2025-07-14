import mysql.connector

# Connect to MySQL (no DB selected yet)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DataScience" 
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS fantasy")
print("✅ Database 'fantasy' created.")

cursor.close()
conn.close()

