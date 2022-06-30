import os
import urllib.parse
import json
import sqlite3

def main():
    with open('README.md', 'a') as readme:
        readme.write("# Whats Included")
    for root, dirs, files in os.walk(r'filters/'):
        for file in files:
            if file.endswith('.txt'):
                    if (isBlacklisted(file) == True):
                        print("🔴 List is blacklisted")
                        blacklist(file)
                    elif(isWhitelisted(file) == True):
                        print("✅List is whitelisted")
                        whitelist(file)
                        output = os.path.join(root, file)
                        encoded = urllib.parse.quote(output)
                        with open('main.txt', 'a') as main:
                            main.write("\n!#include " + encoded)
                        with open('README.md', 'a') as readme:
                            readme.write("\n- "+file)
                    else:
                        print("No data on the list ¯\_(ツ)_/¯")
                    

def blacklist(file):
    try:
        database = 'database/filters.db'
        connection = sqlite3.connect(database)
        cur = connection.cursor()
        delete = "DELETE FROM whitelist(filter_name) VALUES(?);"
        add = "INSERT INTO blacklist(filter_name) VALUES(?);"
        cur.execute(add, (file,))
        connection.commit()
        connection.close()
    except:
        print("List is already blacklisted")

def whitelist(file):
    try:
        database = 'database/filters.db'
        connection = sqlite3.connect(database)
        cur = connection.cursor()
        delete = "DELETE FROM blacklist(filter_name) VALUES(?);"
        add = "INSERT INTO whitelist(filter_name) VALUES(?);"
        cur.execute(add, (file,))
        connection.commit()
        connection.close()
    except:
        print("List is already whitelisted")

def isWhitelisted(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT * FROM whitelist WHERE filter_name = (?);"
    cur.execute(read, (file,))
    filters = cur.fetchall()
    for i in range(len(filters)):
        for filt in filters[i]:
            if(file in filt):
                return True
            else:
                return False
    connection.close()


def isBlacklisted(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT * FROM blacklist WHERE filter_name = (?);"
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