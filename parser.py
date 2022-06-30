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
                if (isDisabled(file) == True):
                    disable(file)
                elif(isEnabled(file) == True):
                    enable(file)
                    output = os.path.join(root, file)
                    encoded = urllib.parse.quote(output)
                    with open('main.txt', 'a') as main:
                        main.write("\n!#include " + encoded)
                    with open('README.md', 'a') as readme:
                        readme.write("\n- "+file)
                else:
                    print("No data on the list ¯\_(ツ)_/¯")
def toggle(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT * FROM filters WHERE filter_name = (?);"
    cur.execute(read, (file,))
    filters = cur.fetchall()
    status='disabled'
    delete = "UPDATE filters SET filter_status=(?) WHERE filter_name=(?);"
    for i in range(len(filters)):
        for filt in filters[i]:
            print(filt)
            cur.execute(delete,(status,file,))
            if(file in filt):
                return True
            else:
                return False

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

def isEnabled(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT * FROM enabled WHERE filter_name = (?);"
    cur.execute(read, (file,))
    filters = cur.fetchall()
    for i in range(len(filters)):
        for filt in filters[i]:
            if(file in filt):
                return True
            else:
                return False
    connection.close()


def isDisabled(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT * FROM disabled WHERE filter_name = (?);"
    cur.execute(read, (file,))
    filters = cur.fetchall()
    for i in range(len(filters)):
        for filt in filters[i]:
            if(file in filt):
                return True
            else:
                return False
    connection.close()
main()