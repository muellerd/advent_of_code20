import itertools

rows = []

with open("C:\\Privat\\advent_of_code20\\puzzle14\\input1.txt") as f:
    for line in f:
        rows.append(line.strip())

#print(rows)

memory = {}
currentMask = ""
for line in rows:
    split = line.split(' = ')
    if 'mask' in split[0]:
        currentMask = split[1].strip()
    else:
        # value in bit
        value = int(split[1])

        # replace in memory
        memoryPosition = split[0][4:-1]

        memoryResult = ''
        memoryPositionBit = format(int(memoryPosition), '036b')
        for i in range(0, len(memoryPositionBit)):
            maskBit = currentMask[i]
            bitBit = memoryPositionBit[i]
            if maskBit == '0':
                memoryResult += memoryPositionBit[i]
            if maskBit == '1':
                memoryResult += '1'
            if maskBit == 'X':
                memoryResult += 'X'

        numberOfX = memoryResult.count('X')
        # create different memory addresses
        a = [range(0,2)]*numberOfX
        floatingVersions = tuple(itertools.product(*a))

        memoryAddresses = []
        memoryResultArray = list(memoryResult)
        for tple in floatingVersions:
            tupleIndex = 0
            newMemoryAddress = []
            for i in memoryResultArray:
                if i == 'X':
                    newMemoryAddress.append(str(tple[tupleIndex]))
                    tupleIndex += 1
                else:
                    newMemoryAddress.append(i)
            memoryAddresses.append(''.join(newMemoryAddress))

        for memoryAddress in memoryAddresses:
            memoryPos = int(memoryAddress, 2)
            if not memoryPos in memory:
                memory[memoryPos] = 0
            memory[memoryPos] = value

sum = 0
for key in memory:
    sum += memory[key]

print("Sum of all values in memory: " + str(sum))
