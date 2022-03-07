devmod = 0

def printdev(x):
    if devmod == 1:
        print(x)

i=0
while i == 0:
    result = ""
    variables1 = int(input("Enter the first number:\n"))
    operation = input('Please select the operation: (*, /, +, -)\n')
    variables2 = int(input("Enter the second number:\n"))

    if operation == '*':
        result = variables1*variables2
    elif operation == "/":
        result = variables1/variables2
    elif operation == "+":
        result = variables1+variables2
    elif operation == "-":
        result = variables1-variables2

    printdev(result)
    if result == 31:
        result = 'sjsjsjsjsjsjssjsjsjsjsjsjsjssjsjsjsj'
    print(f'{variables1} {operation} {variables2}  = {result}')

    e=0
    while e == 0:
        cont = str(input('Do you want to make a new transaction? ([Y]es [N]o)\n'))
        if cont.lower() == "y":
            e += 1
        elif cont.lower() == "n":
            i +=1
            e +=1
        else:
            print('Please enter a valid value')
            continue