listOfGroups = []

with open("C:\\Privat\\advent_of_code20\\puzzle6\\input1.txt") as f:
    group = []
    for line in f:
        line = line.strip()
        if line == '':
            listOfGroups.append(group)
            group = []
            continue
        for char in line:
            if not char in group:
                group.append(char)
    listOfGroups.append(group)

print(listOfGroups)

sum = 0
i = 0
while i < len(listOfGroups):
    sum += len(listOfGroups[i])
    i += 1

print("Total sum of yes answers: " + str(sum))


