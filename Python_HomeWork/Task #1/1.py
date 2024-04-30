while True:
    x = input("Enter the number: ")
    if x == "exit":
        break
    elif x.isdigit():
        print(f"Length of the entered number: {len(x)}")
    else:
        print("You did not enter a number")
