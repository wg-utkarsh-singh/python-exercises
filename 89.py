import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.execute("SELECT country FROM countries WHERE area >= 2000000")
row = cur.fetchall()
for i in row:
    print(i[0])
conn.close()
