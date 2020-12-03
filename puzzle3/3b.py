items = []

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

with open("C:\\Privat\\advent_of_code20\\puzzle3\\input1.txt") as f:
    for line in f:
        items.append(line.strip())

multiply = 1

for slope in slopes:
    right = slope[0]
    down = slope[1]

    treecount = 0
    poscount = 0

    i = 0
    while i < len(items):
        item = items[i]
        if poscount > len(item) - 1:
            poscount = poscount - len(item)
        char = item[poscount]
        if char == '#':
            treecount += 1
        poscount += right

        i += down

    print("Treecode for slope " + str(slope) + ": " + str(treecount))
    multiply *= treecount

print("Multiply: " + str(multiply))
