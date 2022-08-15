#Recursion is calling a function within itself
import _Art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}


def calculator():
    print(_Art.calulator)
    chain_operation = True
    num1 = float(input("Enter the first number: "))

    for symbol in operations:
        print(symbol)

    while chain_operation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Enter the second number: "))

        calc_fn = operations[operation_symbol]
        answer = calc_fn(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or 'n' to exit: ").lower() == "y":
            num1 = answer
        else:
            chain_operation = False
            calculator()


calculator()
