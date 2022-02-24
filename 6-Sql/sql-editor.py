devmod = 1

def printdev(x):
    if devmod == 1:
        print(x)

import sqlite3

database = sqlite3.connect('database.sqlite')
db = database.cursor()


choose = int(input("""
[1]- Create Database

Select your action:  
"""))

while True:
    if choose == 1:
        c_db = input('Enter the name of the database you want to create: ')
        c_db_tbl = input('What is the name of the column you will add to the database you created? ')
        db.execute("CREATE TABLE IF NOT EXISTS %s (%s)"% (c_db,c_db_tbl))
    break

database.commit()
database.close()