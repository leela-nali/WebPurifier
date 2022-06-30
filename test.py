import mysql.connector

database = 'database/filters.db'
connection = sqlite3.connect(database)
cur = connection.cursor()

table_list = [a for a in cur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")]
print(table_list)
connection.close()



def addFilter(file):
        add = "INSERT INTO whitelist (filter_name) VALUES (%s)"
        cur.execute(add)
        
