devmod = 0

def printdev(x):
    if devmod == 1:
        print(x)

import random
user_dice = int(random.choice([1,2,3,4,5,6]))
pc_dice = int(random.choice([1,2,3,4,5,6]))
printdev(f'User: {user_dice}\nPc: {pc_dice}')

if user_dice > pc_dice:
    print(f'You won\n Your dice: {user_dice}\n Pc dice: {pc_dice}')
elif user_dice < pc_dice:
    print(f'You lose\n Your dice: {user_dice}\n Pc dice: {pc_dice}')
elif user_dice == pc_dice:
    print(f'Draw\n Your dice: {user_dice}\n Pc dice: {pc_dice}')