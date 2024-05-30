import random

list_el = [
    100,
    400,
    500,
    10,
    50,
    "Банан",
    "Клубника",
    "Камень",
    "Морковь",
    "Огурец",
    "Пицца",
]


def random_elements(list_elements):
    el1 = random.choice(list_elements)
    list_elements.remove(el1)
    el2 = random.choice(list_elements)
    return el1, el2


print(random_elements(list_el))
