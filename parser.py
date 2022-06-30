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
                    elif(isWhitelisted(file) == True):
                        print("✅List is whitelisted")
                        output = os.path.join(root, file)
                        encoded = urllib.parse.quote(output)
                        with open('main.txt', 'a') as main:
                            main.write("\n!#include " + encoded)
                        with open('README.md', 'a') as readme:
                            readme.write("\n- "+file)
                    else:
                        print("No data on the list ¯\_(ツ)_/¯")
                    

def blacklist(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    delete = """DELETE FROM whitelist(filter_name) VALUES(?);"""
    add = """INSERT INTO blacklist(filter_name) VALUES(?);"""
    cur.execute(add, (file,))
    connection.commit()
    connection.close()
    cur.close()

def whitelist(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    delete = """DELETE FROM blacklist(filter_name) VALUES(?);"""
    add = """INSERT INTO whitelist(filter_name) VALUES(?);"""
    cur.execute(add, (file,))
    connection.commit()
    connection.close()
    cur.close()


def isWhitelisted(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT filter_name FROM whitelist;"
    cur.execute(read)
    filters = cur.fetchall()
    if(file in filters):
        print('whitelist TRUE')
        return True
    else:
        print('whitelist FALSE')
        return False
    connection.close()
    cur.close()


def isBlacklisted(file):
    database = 'database/filters.db'
    connection = sqlite3.connect(database)
    cur = connection.cursor()
    read = "SELECT filter_name FROM blacklist;"
    cur.execute(read)
    filters = cur.fetchall()
    if(file in filters):
        print('blacklist TRUE')
        return True
    else:
        print('blacklist FALSE')
        return False
    connection.close()
    cur.close()

main()