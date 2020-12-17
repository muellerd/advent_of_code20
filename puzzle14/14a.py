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
        bit = format(int(split[1]), '036b')
        # bit through mask
        maskl = len(currentMask)
        bitl = len(bit)

        result = ''

        #print(bit)
        #print(currentMask)

        for i in range(0, len(bit)):
            maskBit = currentMask[i]
            bitBit = bit[i]
            if maskBit != 'X':
                result += maskBit
            else:
                result += bitBit

        #print(result)

        toWrite = int(result, 2)

        # replace in memory
        memoryPosition = split[0][4:-1]
        if not memoryPosition in memory:
            memory[memoryPosition] = 0
        memory[memoryPosition] = toWrite

#print(memory)

sum = 0
for key in memory:
    sum += memory[key]

print("Sum of all values in memory: " + str(sum))
