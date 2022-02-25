devmod = 1

def printdev(x):
    if devmod == 1:
        print(x)

def factorial(n, fact=1):
    for i in range(1, n + 1):
        fact *= i

    return fact

x = int(input('Enter the number:\t'))
print(f'Factorial of {x}: {factorial(x)}')