from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Division by zero, not possible!"
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    number_1 = float(input("What's the first number?: "))
    should_continue = True
    while should_continue:
        for op in operations:
            print(op, end=" ")
        operation_symbol = input("Pick an operation: ")
        number_2 = float(input("What's the next number?: "))
        chosen_operation = operations[operation_symbol]
        answer = round(chosen_operation(number_1, number_2), 2)

        print(f"{number_1} {operation_symbol} {number_2} = {answer}")

        next_choice = input(
            f"Type 'y' to continue calculating with {answer},\nType 'n' to exit,\nType 'r' to reset: ").lower()
        if next_choice == "y":
            number_1 = answer
        elif next_choice == "r":
            calculator()
        else:
            should_continue = False
            print("Goodbye...")


calculator()
