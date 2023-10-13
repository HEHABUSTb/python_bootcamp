from Day_10_Art import logo


# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def minus(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2

def calculation():
    print(logo)
    operations = {'+': add,
                  '-': minus,
                  '*': multiply,
                  '/': divide
                  }

    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)

    terminated = False
    while terminated is False:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        result = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        option = input(f"Type 'y' to continue calculating with {result} or 'n' to start a new calculation: ")
        if option == 'y':
            num1 = result
        elif option == 'n':
            terminated = True
            calculation()
        else:
            terminated = True

calculation()