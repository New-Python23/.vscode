while True:
    num1 = input("Please enter a number: ")
    num2 = input("Please enter another number: ")
    num1 = int(num1)
    num2 = int(num2)
    arithmetic = input("Please enter an arithmetic: ")
    if arithmetic == '+':
        result = num1 + num2
    elif arithmetic == '-':
        result = num1 - num2
    elif arithmetic == '*':
        result = num1 * num2
    elif arithmetic == '/':
        result = num1 / num2
    print(result)