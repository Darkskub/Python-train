set1 = {6, 31, 14, 25, 19, 3, 55}
set2 = {30, 22, 6, 79, 25}
set3 = {9, 1, 22, 19, 30}

setUnion1 = set1 | set2
setUnion2 = setUnion1 | set3
listUnion = list(set1) + list(set2) + list(set3)

notInSet = []
for i in range(len(setUnion2)):
    count = 0
    for k in range(len(listUnion)):
        if listUnion[k] == list(setUnion2)[i]:
            count += 1
            if count > 1:
                notInSet.append(listUnion[k])

notInSetSum = 0
setUnion2Sum = 0

for i in range(len(notInSet)):
    notInSetSum += notInSet[i]
for i in range(len(setUnion2)):
    setUnion2Sum += list(setUnion2)[i]

print(f"Difference of all elements of a set and a list: {setUnion2Sum - notInSetSum}")
