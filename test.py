import sqlite3
file="filters-2021.txt"
database = 'database/filters.db'
connection = sqlite3.connect(database)
cur = connection.cursor()
read = "SELECT * FROM whitelist WHERE filter_name = (?);"
cur.execute(read, (file,))
filters = cur.fetchall()
for f in filters:
  print(f)
if file in filters:
        print(filters)
        print ("TRUE")
else:
        print("FALSE")
connection.close()
