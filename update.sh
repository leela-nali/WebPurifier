git submodule update --recursive --remote
rm -rf main.txt
rm -rf README.md
touch main.txt
touch README.md
cat header.txt >> main.txt
python3 parser.py
git add .
git commit -m "updated main.txt"
git push
