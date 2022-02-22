devmod = 0

def printdev(x):
    if devmod == 1:
        print(x)

result = ""
variables1 = int(input("Enter the first number:\n"))
operation = input('Please select the operation: (*, /, +, -)\n')
variables2 = int(input("Enter the second number:\n"))

if operation == ['x','X','*']:
    result = variables1*variables2
elif operation == "/":
    result = variables1/variables2
elif operation == "+":
    result = variables1+variables2
elif operation == "-":
    result = variables1-variables2

printdev(result)
print(f'{variables1} {operation} {variables2}  = {result}')