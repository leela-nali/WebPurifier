import mysql.connector

database = 'database/filters.db'
connection = sqlite3.connect(database)
cur = connection.cursor()

class Filter:
        def __init__(self):
                self.whitelist = whitelist(file)(file)

        def whitelist(file):
                add = "INSERT INTO whitelist (filter_name) VALUES (%s)"
                cur.execute(add, file)
                connection.close()
