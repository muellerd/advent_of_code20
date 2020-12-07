parentToChildrenBags = {}

with open("C:\\Privat\\advent_of_code20\\puzzle7\\input1.txt") as f:
    for line in f:
        line = line.strip()
        print(line)

        lineSplit = line.split('contain')
        startingColorSplit = lineSplit[0].split(' ')
        startingColor = startingColorSplit[0] + ' ' + startingColorSplit[1]
        if not startingColor in parentToChildrenBags:
            parentToChildrenBags[startingColor] = []
        print(lineSplit)
        lineSplit2 = lineSplit[1].split(',')
        print(lineSplit2)
        for bag in lineSplit2:
            if 'no other bags' in bag:
                continue
            bagSplit = bag.strip().split(' ')
            bagString = bagSplit[1] + ' ' + bagSplit[2]
            if not bagString in parentToChildrenBags[startingColor]:
                parentToChildrenBags[startingColor].append((bagString, bagSplit[0]))


print(parentToChildrenBags)

baggs = []

def recurse(parentToChildrenBags, bagTuples):
    for bagTuple in bagTuples:
        i = 0
        while i < int(bagTuple[1]):
            recurse(parentToChildrenBags, parentToChildrenBags[bagTuple[0]])
            i += 1
            baggs.append(bagTuple[0])


recurse(parentToChildrenBags, parentToChildrenBags['shiny gold'])
#print(baggs)
print("Number of bags that are contained in a shiny gold bag: " + str(len(baggs)))
