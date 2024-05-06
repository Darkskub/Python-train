import random

list_el = [100, 400, 500, 10, 50, "Банан", "Клубника", "Камень", "Морковь", "Огурец", "Пицца"]

def random(list_el):
    el1 = random.choice(list_el)
    list_el.remove(el1)
    el2 = random.choice(list_el)
    return el1, el2

print(random(list_el))
