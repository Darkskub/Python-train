ship = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
while True:
    x = input("Enter coordinate: ")
    if x == "exit":
        break
    elif x[0].isalpha() and x[1:].isdigit() and len(x) == 2:
        if ship.find(x) >= 0 or ship.find(x.upper()) >= 0:
            print("You got it")
        else:
            print("You missed")
    else:
        print("You did not enter a coordinate")
