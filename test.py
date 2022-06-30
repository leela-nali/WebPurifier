import sqlite3

database = 'database/filters.db'
connection = sqlite3.connect(database)
cur = connection.cursor()
read = "SELECT filter_name FROM whitelist;"
cur.execute(read)
filters = cur.fetchall()
print(filters)
connection.close()