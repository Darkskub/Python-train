while True:
    x = input("Enter the number: ")
    if x == "exit":
        break
    elif x.isdigit():
        x = int(x)
        neg = 0
        pos = 0
        for x in range(-x, x + 1):
            print(x)
            if x < 0:
                neg += x
            else:
                pos += x
        print(
            f"The sum of negative numbers is {neg} and the sum of positive numbers is {pos}"
        )
    else:
        print("You did not enter a number")
