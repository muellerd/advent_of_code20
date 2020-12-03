items = []

with open("C:\\Privat\\advent_of_code20\\puzzle2\\input1.txt") as f:
    for line in f:
        items.append(line.strip())

wrongPasswords = 0
for item in items:
    itemsplit = item.split(':')
    #print(itemsplit)

    firstItemSplit = itemsplit[0].split(' ')
    character = firstItemSplit[1]
    firstItemSplitFirstItem = firstItemSplit[0].split('-')
    firstPos = int(firstItemSplitFirstItem[0])
    secondPos = int(firstItemSplitFirstItem[1])

    if character == itemsplit[1].strip()[firstPos-1] and character == itemsplit[1].strip()[secondPos-1]:
        wrongPasswords += 1
        print(item + " is wrong.")
    else:
        if character != itemsplit[1].strip()[firstPos-1] and character != itemsplit[1].strip()[secondPos-1]:
            wrongPasswords += 1
            print(item + " is wrong.")

print("Number of wrong passwords: " + str(wrongPasswords))
print("Number of valid passwors:" + str(len(items) - wrongPasswords))
