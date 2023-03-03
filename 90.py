import sqlite3

import pandas

conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.execute("SELECT * FROM countries WHERE area >= 2000000")
row = cur.fetchall()
conn.close()

df = pandas.DataFrame.from_records(row)
df.columns = ["Rank", "Country", "Area", "Population"]
df.to_csv("countries_big_area.csv", index=False)
