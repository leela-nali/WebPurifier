import os
import urllib.parse

for root, dirs, files in os.walk(r'filters/'):
    for file in files:
        if file.endswith('.txt'):
            output = os.path.join(root, file)
            encoded = urllib.parse.quote(output)
            with open('main.txt', 'a') as main:
                main.write("!#include " + encoded + "\n")
