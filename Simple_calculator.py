print('Enter the first number')
num1 = int(input())
print('Enter the second number')
num2 = int(input())
print('Enter the operation you want(+,-,/,*')
operation = input()
if operation == '+':
    print('Result=', num1 + num2)
elif operation == '-':
    print('Result=', num1 - num2)
elif operation == '*':
    print('Result=', num1 * num2)
elif operation == '/':
    print('Result=', num1 / num2)
