childToParentBags = {}

def printDictionaryChildren(bagsdict, bag, list):
    if bag in bagsdict:
        for bg in bagsdict[bag]:
            if not bg in list:
                list.append(bg)
            printDictionaryChildren(bagsdict, bg, list)
    print(bag)

with open("C:\\Privat\\advent_of_code20\\puzzle7\\example1.txt") as f:
    for line in f:
        line = line.strip()
        print(line)

        lineSplit = line.split('contain')
        startingColorSplit = lineSplit[0].split(' ')
        startingColor = startingColorSplit[0] + ' ' + startingColorSplit[1]
        print(lineSplit)
        lineSplit2 = lineSplit[1].split(',')
        print(lineSplit2)
        for bag in lineSplit2:
            if 'no other bags' in bag:
                continue
            bagSplit = bag.strip().split(' ')
            bagString = bagSplit[1] + ' ' + bagSplit[2]
            if bagString not in childToParentBags:
                childToParentBags[bagString] = []
            childToParentBags[bagString].append(startingColor)

print(childToParentBags)

shinyGoldParentsList = []
printDictionaryChildren(childToParentBags, 'shiny gold', shinyGoldParentsList)
print(shinyGoldParentsList)
print("Number of bag colors that can contain shiny gold bags: " + str(len(shinyGoldParentsList)))
