import sqlite3

def blacklist(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    add = "INSERT INTO blacklist (filter_name) VALUES (%s)"
    delete = "DELETE FROM whitelist WHERE (filter_name) = "
    cur.execute(add, file)
    cur.execute(delete, file)
    connection.close()

def whitelist(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    add = "INSERT INTO whitelist (filter_name) VALUES (%s)"
    delete = "DELETE FROM blacklist WHERE (filter_name) = "
    cur.execute(add, file)
    cur.execute(delete, file)
    connection.close()

blacklist("Test.txt")