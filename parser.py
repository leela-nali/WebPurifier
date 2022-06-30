# Imports
import os
import urllib.parse
import json
import mysql.connector
import Filter

# Variables
database = 'database/filters.db'
connection = mysql.connect(database)
cur = connection.cursor()

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
    with open("json/blacklist.json", "w") as blacklist:
        blacklist.write(file)
def whitelist(file):
    Filter().whitelist(file)
    with open("json/whitelist.json", "w") as whitelist:
        whitelist.write(file)

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



class Filter:
        def __init__(self):
                self.whitelist = whitelist(file)(file)

        def whitelist(file):
                add = "INSERT INTO whitelist (filter_name) VALUES (%s)"
                cur.execute(add, file)
                connection.close()
main()