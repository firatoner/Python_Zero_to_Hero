devmod = 1

def printdev(x):
    if devmod == 1:
        print(x)

import random
x = int(random.choice([1,2,3,4,5,6]))
printdev(x)