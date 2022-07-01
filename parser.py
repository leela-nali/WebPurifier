import os
import urllib.parse
import sqlite3
import sys
import logging
logger = logging.getLogger(__name__)
def main():
    with open('README.md', 'a') as readme:
        readme.write("# Whats Included")
        logger.info("added 'whats included' header")
    for root, dirs, files in os.walk(r'filters/'):
        for file in files:
            if file.endswith('.txt'):
                if (exists(file)):
                    if (breaks(file == True)):
                        disable(file)
                    else:
                        if (filter_status(file) == "DISABLED"):
                                print(file + " is disabled")
                        elif(filter_status(file) == "ENABLED"):
                            output = os.path.join(root, file)
                            encoded = urllib.parse.quote(output)
                            with open('main.txt', 'a') as main:
                                main.write("\n!#include " + encoded)
                            with open('README.md', 'a') as readme:
                                readme.write("\n- "+file)
                        elif():
                            print("No data on the list "+ file)
                else:
                    print(file + "doesnt exist. Moving adding now")
                    addList(file)
def toggle(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "  WHERE filter_name = (?);"
    cur.execute(read, (file,))
    filters = cur.fetchall()
    for i in range(len(filters)):
        for filt in filters[i]:
            if(filt == "DISABLED"):
                enable = "UPDATE filters SET filter_status='ENABLED' WHERE filter_name=(?);"
                cur.execute(enable,(file,))
                connection.commit()
                print(file + " is now enabled")
                connection.close()
            elif(filt == "ENABLED"):
                disable = "UPDATE filters SET filter_status='DISABLED' WHERE filter_name=(?);"
                cur.execute(disable,(file,))
                connection.commit()
                print(file + " is now disabled")
                connection.close()
            elif(filt == "NULL"):
                disable = "UPDATE filters SET filter_status='DISABLED' WHERE filter_name=(?);"
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
            if(filt == "ENABLED"):
                return "ENABLED"
            elif(filt == "DISABLED"):
                return "DISABLED"
            else:
                continue
    connection.close()

def addList(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    add =  "INSERT INTO filters(filter_name, filter_status) VALUES (?, ?);"
    val = (file, "DISABLED")

    cur.execute(add,(val))
    connection.commit()
    connection.close()

def disable(file):
    try:
        database = 'database/filters.db'
        connection = sqlite3.connect(database)
        cur = connection.cursor()
        disable = "UPDATE filters SET filter_status='DISABLED' WHERE filter_name=(?);"
        cur.execute(disable,(file,))
        connection.commit()
        print(file + " is now disabled")
        connection.close()
    except:
        print("List is already enabled")

def exists(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT filter_name FROM filters WHERE filter_name = (?);"
    cur.execute(read, (file,))
    filters = cur.fetchall()
    for i in range(len(filters)):
        for filt in filters[i]:
            if(filt):
                return True
            else:
                return False
    connection.close()

def isDisabled(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT filter_status FROM filters WHERE filter_name = (?);"
    cur.execute(read, (file,))
    filters = cur.fetchall()
    for i in range(len(filters)):
        for filt in filters[i]:
            if(filt == "DISABLED"):
                return True
            else:
                return False
    connection.close()

def breaks(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT filter_notes FROM filters WHERE filter_name = (?);"
    cur.execute(read, (file,))
    filters = cur.fetchall()
    for i in range(len(filters)):
        for filt in filters[i]:
            if(filt == "BREAKS"):
                return True
            else:
                return False
    connection.close()
main()