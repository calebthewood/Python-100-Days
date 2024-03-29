from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))
    for operation in operations: print(operation)

    operation_symbol = input("Pick an operation symbol from the line above: ")
    calc_func = operations[operation_symbol]
    answer = calc_func(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    prompt = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")

    while prompt == 'y':
        operation_symbol = input("Pick an operation: ")
        num = float(input("What's the next number?: "))
        calc_func = operations[operation_symbol]
        prev_answer = answer
        answer = calc_func(prev_answer, num)
        print(f"{prev_answer} {operation_symbol} {num} = {answer}")

        prompt = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")

        if prompt == "n":
            return calculator()

calculator()