listOfGroupAnswers = []
listOfGroupSize = []

with open("C:\\Privat\\advent_of_code20\\puzzle6\\input1.txt") as f:
    groupDict = {}
    groupSizeCount = 0
    for line in f:
        line = line.strip()
        if line == '':
            listOfGroupAnswers.append(groupDict)
            groupDict = {}
            listOfGroupSize.append(groupSizeCount)
            groupSizeCount = 0
            continue
        groupSizeCount += 1
        for char in line:
            if not char in groupDict:
                groupDict[char] = 1
            else:
                groupDict[char] += 1
    listOfGroupAnswers.append(groupDict)
    listOfGroupSize.append(groupSizeCount)

print(listOfGroupAnswers)
print(listOfGroupSize)

sum = 0
i = 0
while i < len(listOfGroupAnswers):
    dict = listOfGroupAnswers[i]
    size = listOfGroupSize[i]
    for key in dict:
        if dict[key] == size:
            sum += 1

    i += 1

print("Total sum of yes answers: " + str(sum))

