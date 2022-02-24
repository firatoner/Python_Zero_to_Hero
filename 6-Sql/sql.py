devmod = 1

def printdev(x):
    if devmod == 1:
        print(x)

import sqlite3

database = sqlite3.connect('database.sqlite')
db = database.cursor()

db.execute("CREATE TABLE IF NOT EXISTS Rehber (Name,Phone Number)")

#name,number = "Fıratt",'053131'

while True:
    name = input('Enter your name:\n')
    if name == "":
        print('Pls enter vauld value!!!')
        continue
    else:
        break

while True:
    number = input('Enter your number:\n')
    if number == "":
        print('Pls enter vauld value!!!')
        continue
    else:
        break

result = [name,number]
printdev(result)

db.execute("INSERT INTO Rehber VALUES (?,?)",result)

database.commit()
database.close()