import sqlite3

conn = sqlite3.connect()
cursor = conn.execute()
rows =  cursor.fetchall()
rows