
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


chain_operation = True
use_answer = True
while chain_operation:
    num1 = int(input("Enter the first number: "))

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("Enter the second number: "))

    calc_fn = operations[operation_symbol]
    answer = calc_fn(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer} or 'n' to exit: ").lower() == "y":
        while use_answer:
            num1 = answer
            num2 = int(input("Enter next number: "))
            operation_symbol = input("Pick an operation: ")
            calc_fn = operations[operation_symbol]
            answer = calc_fn(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")

            if input("Type 'y' to continue calculating with {answer} or 'n' to exit: ").lower() == "n":
                use_answer = False
