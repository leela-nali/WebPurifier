import os
import urllib.parse
import json
import mysql.connector

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

def isWhitelisted(file):
    with open('json/whitelist.json', 'r') as whitelist:
        wl_data = json.load(whitelist)
        if(file in wl_data):
            return True
        else:
            return False
        whitelist.close()
def isBlacklisted(file):
    with open('json/blacklist.json', 'r') as blacklist:
        bl_data = json.load(blacklist)
        if(file in bl_data):
            return True
        else:
            return False
        blacklist.close()
main()