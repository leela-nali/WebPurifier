import os

for root, dirs, files in os.walk(r'filters/'):
    for file in files:
        if file.endswith('.txt'):
            output = os.path.join(root, file)
            encoded = output.replace(" ", "%20")
            with open('main.txt', 'a') as main:
                main.write("!#include " + encoded + "\n")
