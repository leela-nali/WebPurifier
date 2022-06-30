import os
import urllib.parse
import json

def main():
    with open('README.md', 'a') as readme:
        readme.write("# Whats Included")
    for root, dirs, files in os.walk(r'filters/'):
        for file in files:
            if file.endswith('.txt'):
                try:
                    if (isBlacklisted(file) == True):
                        print("🔴 List is blacklisted")
                    elif(isBlacklisted(file) == False):
                        whitelist(file)
                    elif(isWhitelisted(file) == True):
                        print("✅List is whitelisted")
                        output = os.path.join(root, file)
                        encoded = urllib.parse.quote(output)
                        with open('main.txt', 'a') as main:
                            main.write("\n!#include " + encoded)
                        with open('README.md', 'a') as readme:
                            readme.write("\n- "+file)
                    elif(isWhitelisted(file) == False):
                        blacklist(file)
                    else:
                        print("No data on the list ¯\_(ツ)_/¯")
                except:
                    print("Exception thrown. List validation failed.")

def blacklist(file):
    with open("json/whitelist.json", "r") as whitelist:
        whitelist.pop(file)
    with open("json/blacklist.json", "w") as blacklist:
        blacklist.write(file)
def whitelist(file):
    with open "json/blacklist.json", "r" as blacklist:
        blacklist.pop(file)
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
main()