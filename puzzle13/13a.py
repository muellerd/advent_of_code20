lines = []
with open("C:\\Privat\\advent_of_code20\\puzzle13\\input1.txt") as f:
    for line in f:
        line = line.strip()
        lines.append(line)

print(lines)
earliest = int(lines[0])
ids = []
for id in lines[1].split(','):
    if id != 'x':
        ids.append(int(id))

ids = sorted(ids)
print(ids)

found = False

i = 0
toCheck = 0
bestId = 0
while not found:
    toCheck = earliest + i
    for id in ids:
        if toCheck % id == 0:
            found = True
            bestId = id
            break
    i += 1

wait = toCheck - earliest

print("The earliest possible bus has ID " + str(bestId) + ", time to depart: " + str(wait))
print("Multiplication: " + str(wait * bestId))
