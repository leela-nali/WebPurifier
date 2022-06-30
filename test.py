import sqlite3



def toggle():
    file = "a.txt"
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT * FROM filters WHERE filter_name = (?);"
    cur.execute(read, (file,))
    filters = cur.fetchall()
    print(filters)
    toggle = "UPDATE filters SET filter_status = enabled WHERE filter_name = (?);"
    cur.execute(toggle, (file,))
    for i in range(len(filters)):
        for filt in filters[i]:
            if(file in filt):
                print(file)
            else:
                return
    connection.close()

toggle()