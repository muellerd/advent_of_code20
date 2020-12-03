items = []

with open("C:\\Privat\\advent_of_code20\\puzzle2\\input1.txt") as f:
    for line in f:
        items.append(line.strip())
        #print(line.strip())

wrongPasswords = 0

for item in items:
    itemsplit = item.split(':')
    #print(itemsplit)

    firstItemSplit = itemsplit[0].split(' ')
    character = firstItemSplit[1]
    firstItemSplitFirstItem = firstItemSplit[0].split('-')
    min = int(firstItemSplitFirstItem[0])
    max = int(firstItemSplitFirstItem[1])

    count = 0
    for l in itemsplit[1].strip():
        if l == character:
            count += 1

    #print(item + ": " + character + " count is " + str(count))

    if count < min or count > max:
        wrongPasswords += 1
        print(item + " is wrong. (" + str(count) + ")")

print("Number of wrong passwords: " + str(wrongPasswords))
print("Number of valid passwors:" + str(len(items) - wrongPasswords))

