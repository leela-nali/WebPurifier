import os
import urllib.parse
import json
import sqlite3
import sys

#switcher = {
#    add: addList(),
#    delete: deleteList(),
#    whitelist: whitelist(),
#    blacklist: blacklist(),
#    update: update()
#    }

#def switch(command):
#    return switcher.get(command, default)()

#for arg in sys.argv:
#    switch(arg)

def main():
    with open('README.md', 'a') as readme:
        readme.write("# Whats Included")
    for root, dirs, files in os.walk(r'filters/'):
        for file in files:
            if file.endswith('.txt'):
                if (filter_status(file) == "Disabled"):
                    print(file + " is disabled")
                elif(filter_status(file == "Enabled")):
                    enable(file)
                    output = os.path.join(root, file)
                    encoded = urllib.parse.quote(output)
                    with open('main.txt', 'a') as main:
                        main.write("\n!#include " + encoded)
                    with open('README.md', 'a') as readme:
                        readme.write("\n- "+file)
                elif():
                    print("No data on the list "+ file)

def toggle(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT filter_status FROM filters WHERE filter_name = (?);"
    cur.execute(read, (file,))
    filters = cur.fetchall()
    for i in range(len(filters)):
        for filt in filters[i]:
            if(filt == "disabled"):
                enable = "UPDATE filters SET filter_status='enabled' WHERE filter_name=(?);"
                cur.execute(enable,(file,))
                connection.commit()
                print(file + " is now enabled")
                connection.close()
            elif(filt == "enabled"):
                disable = "UPDATE filters SET filter_status='disabled' WHERE filter_name=(?);"
                cur.execute(disable,(file,))
                connection.commit()
                print(file + " is now disabled")
                connection.close()
            elif(filt == "NULL"):
                disable = "UPDATE filters SET filter_status='disabled' WHERE filter_name=(?);"
                cur.execute(disable,(file,))
                connection.commit()
                print(file + " is now disabled")
                connection.close()

def filter_status(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT filter_status FROM filters WHERE filter_name = (?);"
    cur.execute(read, (file,))
    filters = cur.fetchall()
    for i in range(len(filters)):
        for filt in filters[i]:
            if(filt == "Enabled"):
                return "Enabled"
            else:
                return "Disabled"
    connection.close()

def enable(file):
    try:
        database = 'database/filters.db'
        connection = sqlite3.connect(database)
        cur = connection.cursor()
        delete = "DELETE FROM disabled(filter_name) VALUES(?);"
        add = "INSERT INTO enabled(filter_name) VALUES(?);"
        cur.execute(delete, (file,))
        cur.execute(add, (file,))
        connection.commit()
        connection.close()
    except:
        print("List is already enabled")


def isDisabled(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT filter_status FROM filters WHERE filter_name = (?);"
    cur.execute(read, (file,))
    filters = cur.fetchall()
    for i in range(len(filters)):
        for filt in filters[i]:
            if(filt == "Disabled"):
                return True
            else:
                return False
    connection.close()
main()