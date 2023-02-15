
def add(x,y):
    return x+y

def subtr(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

print('Select the operation')
print('1. +')
print('2. -')
print('3. *')
print('4. /')

choice = input('Please enter (+/-/*//): ')

num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))

if choice == '+':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '-':
    print(num1, "-", num2, "=", subtr(num1, num2))

elif choice == '*':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '/':
    print(num1, "/", num2, "=", divide(num1, num2))
    
else:
    print('This is an invalid input')
# Press the green button in the gutter to run the script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
