import sys

print(sys.argv)

if len(sys.argv) == 1:
    print("USAGE: python4 app.py <passwprd>")
else:
    password = sys.argv[1]
    print("Password", password)
