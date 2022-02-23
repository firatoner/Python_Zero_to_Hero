devmod = 0

def printdev(x):
    if devmod == 1:
        print(x)

import random
pc_choice = str(random.choice(["heads","tails"]))
printdev(f'Pc choice {pc_choice}')
user_choice = str(input('Choose your side: (Heads or Tails)\n'))
printdev(f'User Choice {user_choice}')
print(f'Your choice {user_choice.lower()}')

if pc_choice.lower() == user_choice.lower():
    printdev("Pc = User")
    print(f'You won !')
elif pc_choice.lower() != user_choice.lower():
    printdev("Pc != User")
    if  user_choice.lower() != ['heads','tails']:
        print('Please enter a valid value')
    else:
        print(f'You lose !')