items = []

with open("C:\\Privat\\advent_of_code20\\puzzle3\\input1.txt") as f:
    for line in f:
        items.append(line.strip())


treecount = 0
poscount = 0

for item in items:
    if poscount > len(item) - 1:
        poscount = poscount - len(item)
    char = item[poscount]
    #print(char)
    if char == '#':
        treecount += 1
    poscount += 3

print("Number of encountered trees: " + str(treecount))

