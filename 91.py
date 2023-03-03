import sqlite3
import pandas

data = pandas.read_csv("ten_more_countries.txt")

conn = sqlite3.connect("database.db")
cur = conn.cursor()
for index, row in data.iterrows():
    cur.execute(
        "INSERT INTO countries VALUES (NULL,?,?,NULL)", (row["Country"], row["Area"])
    )
conn.commit()
conn.close()
