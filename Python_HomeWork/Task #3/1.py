Addition = lambda a, b: a + b
Subtraction = lambda a, b: a - b
Multiplication = lambda a, b: a * b
Exponentiation = lambda a, b: a**b


def Division(a, b):
    if b == 0:
        raise ValueError("You can't divide by 0")
    return a / b


while True:
    userInput = input(
        "Enter the operation to be performed (example: 2 / 2, 3 ** 5), or exit: "
    ).split(" ")
    if userInput == "exit":
        break
    elif len(userInput) != 3:
        print("An incorrect operation was introduced")
        continue
    elif not userInput[0].isdigit() or userInput[1].isdigit():
        print("An incorrect operation was introduced")
        continue
    else:
        userInput[0] = int(userInput[0])
        userInput[2] = int(userInput[2])

    if userInput[1] == "+":
        print(Addition(userInput[0], userInput[2]))
    elif userInput[1] == "-":
        print(Subtraction(userInput[0], userInput[2]))
    elif userInput[1] == "*":
        print(Multiplication(userInput[0], userInput[2]))
    elif userInput[1] == "**":
        print(Exponentiation(userInput[0], userInput[2]))
    elif userInput[1] == "/":
        try:
            print(Division(userInput[0], userInput[2]))
        except ValueError:
            print("You can't divide by 0")
            continue
    else:
        print("An incorrect operation was introduced")
        continue
