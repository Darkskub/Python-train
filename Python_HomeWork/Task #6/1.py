def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)


assert average_num([1, 2, 3, 4, 5]) == 3.00

assert average_num([1.0, 2.5, 3.0, 4.5]) == 2.75

assert average_num([1, 2.5, 3, 4.5]) == 2.75

assert average_num([0, 0, 0, 0]) == 0.00

assert average_num([-1, -2, -3, -4]) == -2.50

assert average_num(["1", "2", "3", "4"]) == 2.50

assert average_num([1, "2", 3.0, "4.5"]) == 2.63

assert average_num([1, "two", 3, "four"]) == "Bad request"
