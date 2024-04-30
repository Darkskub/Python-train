# Создаем пустой список
l = []

# Получаем количество элементов списка от пользователя
count = int(input("Введите количество элементов в списке: "))

# Получаем элементы списка от пользователя
i = 0
while len(l) < count:
    element = input(f"Введите {len(l) + 1}-й элемент списка: ")
    if not element.isdigit():
        print("Вы ввели не число")
        continue
    l.append(int(element))
    i += 1

print("Список:", l)
