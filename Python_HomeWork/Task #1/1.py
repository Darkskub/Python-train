ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
while True:
    x = input("Enter the number: ")
    if x == "exit":
        break
    elif x.isdigit():
        print(f"Length of the entered number: {len(x)}")
    else:
        print("You did not enter a number")
