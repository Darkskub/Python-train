dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

dctKey = []
dctValue = []

for key, value in dct.items():
    dctKey.append(key)
    dctValue.append(value)

dctValue = set(dctValue)
dctKey = set(dctKey)

dctUnion = dctKey | dctValue

print(f"United sets: {dctUnion}")

# Также можно было использовать dct.keys() и dct.values()
