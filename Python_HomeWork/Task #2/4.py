dictionary = {
    "Имя": [
        "Андрей",
        "Кирилл",
        "Анна",
        "Евгений",
        "Евгений",
        "Александр",
        "Татьяна",
        "Аркадий",
        "Игорь",
        "Кирилл",
    ],
    "Фамилия": [
        "Иванов",
        "Лазарев",
        "Петрова",
        "Надобников",
        "Никитин",
        "Иванов",
        "Никитина",
        "Лихачев",
        "Никитин",
        "Левашев",
    ],
    "Город проживания": [
        "Москва",
        "Омск",
        "Псков",
        "Псков",
        "Москва",
        "Псков",
        "Москва",
        "Омск",
        "Псков",
        "Москва",
    ],
    "Год рождения": [2000, 1987, 2003, 1993, 2001, 2001, 1976, 1957, 1969, 1999],
    "Месяц рождения": [6, 4, 11, 12, 9, 9, 5, 2, 3, 6],
    "Число рождения": [11, 25, 5, 3, 27, 31, 13, 12, 28, 24],
    "Статус": [
        "Студент",
        "Работает",
        "Школьница",
        "Работает",
        "Студент",
        "Студент",
        "Работает",
        "Пенсия",
        "Работает",
        "Студент",
    ],
}

dictionaryNF = []
dictionaryDate = []
dictionaryCity = dictionary["Город проживания"]
dictionaryStatus = dictionary["Статус"]

for i in range(len(dictionary["Фамилия"])):
    dictionaryNF.append(dictionary["Фамилия"][i].upper() + "--" + dictionary["Имя"][i])
    dictionaryDate.append(
        str(dictionary["Год рождения"][i])
        + "-"
        + str(dictionary["Месяц рождения"][i])
        + "-"
        + str(dictionary["Число рождения"][i])
    )

dictionaryNew = {
    "Фамилия Имя": dictionaryNF,
    "Дата рождения": dictionaryDate,
    "Город проживания": dictionaryCity,
    "Статус": dictionaryStatus,
}

for i in range(len(dictionary["Фамилия"])):
    if dictionary["Имя"][i] == "Кирилл":
        dictionaryNF[i] = dictionary["Фамилия"][i].upper() + "--" + "Кириллл"
    else:
        continue

for i in range(len(dictionary["Фамилия"])):
    if dictionary["Фамилия"][i] == "Никитин" or dictionary["Фамилия"][i] == "Никитина":
        dictionaryCity[i] = "Махачкала"
    else:
        continue

dictionaryStatus[dictionaryNF.index("ИВАНОВ--Александр")] = "Работает"

dictionaryStatus.pop(dictionaryNF.index("ЛИХАЧЕВ--Аркадий"))
dictionaryDate.pop(dictionaryNF.index("ЛИХАЧЕВ--Аркадий"))
dictionaryCity.pop(dictionaryNF.index("ЛИХАЧЕВ--Аркадий"))
dictionaryNF.pop(dictionaryNF.index("ЛИХАЧЕВ--Аркадий"))

print("Новый словарь:\n", dictionaryNew)

# {“Фамилия Имя”: [ФАМИЛИЯ--Имя],
# “Дата рождения”: [Г-М-Д], # Формат ГГГГ-ММ-ДД
# “Город проживания”: [],
# “Статус”: []
# }
