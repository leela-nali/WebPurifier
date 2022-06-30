import sqlite3



def toggle():
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT * FROM filters WHERE filter_name = (?);"
    cur.execute(read, (file,))
    filters = cur.fetchall()
    print(filters)
    
    delete = "UPDATE filters SET filter_status='disabled' WHERE filter_name=(?);"
    read = "SELECT * FROM filters WHERE filter_name = (?);"
    cur.execute(read, (file,))
    connection.commit()
    print(filters)

toggle()