from functools import reduce
import operator

ids = []
indices = []

i = 0
with open("C:\\Privat\\advent_of_code20\\puzzle13\\input1b.txt") as f:
    for line in f:
        lines = line.strip().split(',')
        for id in lines:
            if id != 'x':
                ids.append(int(id))
                indices.append(i)
            i += 1

number = 0
value = 0
index = 0
for id in ids:
    if number == 0:
        number = id
        value = id
    else:
        number = reduce(operator.mul, ids[:index])

    while (value + indices[index]) % id != 0:
        value += number

    index += 1

print("Earliest timestamp: " + str(value))
