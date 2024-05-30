while True:
    l = input("Enter a list of numbers separated by spaces: ").split(" ")
    try:
        for i in range(len(l)):
            if l[i].isdigit():
                l[i] = int(l[i])
            else:
                raise ValueError("Wrong datatype")
                break
    except ValueError:
        print("Invalid list entered")
    else:
        break

while True:
    n = input("Enter multiplier: ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Invalid multiplier entered")


def Mult(a: list, b: int = 2) -> list:
    l1 = []
    for i in range(len(a)):
        l1.append(l[i] * b)
    return l1


print(Mult(l))  # Тут без ввода второй переменной
print(Mult(l, n))
