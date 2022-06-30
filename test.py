import sqlite3

database = 'database/filters.db'
connection = sqlite3.connect(database)
cur = connection.cursor()
read = """SELECT * FROM whitelist;"""
cur.execute(read)
connection.commit()
connection.close()