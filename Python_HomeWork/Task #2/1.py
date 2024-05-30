while True:
    count = input("How many elements do you want to enter: ")
    if count.isdigit():
        count = int(count)
        break
    else:
        print("You did not enter a number")

l = []

while len(l) < count:
    element = input(f"Enter the {len(l) + 1}th element of the list: ")
    if not element.isdigit():
        print("You did not enter a number")
        continue
    l.append(int(element))

while True:
    power = input("Enter the power to which you want to raise the elements: ")
    if power.isdigit():
        power = int(power)
        break
    else:
        print("You did not enter a number")

l1 = [l[i] ** power for i in range(count)]

print(f"Initial list of elements: {l}")
print(f"List of elements raised to the {power}th power: {l1}")
