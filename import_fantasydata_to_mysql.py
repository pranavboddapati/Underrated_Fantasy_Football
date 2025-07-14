import pandas as pd
import mysql.connector

# Load your CSV
df = pd.read_csv("fantasy_data.csv")

# Clean column names (optional)
df.rename(columns={
    'Unnamed: 0_level_0_Rk': 'Rk',
    'Unnamed: 4_level_0_Age': 'Age',
    'Rushing_Y/A': 'Rushing_YA',
    'Receiving_Y/R': 'Receiving_YR'
}, inplace=True)

# Connect to 'fantasy' database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="DataScience",  
    database="fantasy"
)
cursor = conn.cursor()

# Create table
cursor.execute("DROP TABLE IF EXISTS fantasy_2024_stats")
cursor.execute("""
CREATE TABLE fantasy_2024_stats (
    Rk INT,
    Player VARCHAR(100),
    Team VARCHAR(10),
    Position VARCHAR(10),
    Age INT,
    GamesPlayed FLOAT,
    Games_GS INT,
    Passing_Cmp INT,
    Passing_Att INT,
    Passing_Yds INT,
    Passing_TD INT,
    Passing_Int INT,
    Rushing_Att INT,
    Rushing_Yds INT,
    Rushing_YA FLOAT,
    Rushing_TD INT,
    Receiving_Tgt INT,
    Receiving_Rec INT,
    Receiving_Yds INT,
    Receiving_YR FLOAT,
    Receiving_TD INT,
    Fumbles_Fmb INT,
    Fumbles_FL INT,
    Scoring_TD INT,
    Scoring_2PM FLOAT,
    Scoring_2PP FLOAT,
    FantasyPoints INT,
    Fantasy_PPR FLOAT,
    Fantasy_DKPt FLOAT,
    Fantasy_FDPt FLOAT,
    Fantasy_VBD FLOAT,
    Fantasy_PosRank INT,
    Fantasy_OvRank FLOAT
)
""")

# Insert rows
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO fantasy_2024_stats VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                                               %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()
print("✅ Data imported to MySQL.")
