instructions = []
lineCount = {}
changeList = []

with open("C:\\Privat\\advent_of_code20\\puzzle8\\input1.txt") as f:
    i = 0
    for line in f:
        line = line.strip()
        instructions.append(line)
        lineCount[i] = 0
        if 'nop' in line or 'jmp' in line:
            changeList.append(i)

        i += 1

print(instructions)
print(lineCount)

cleanAccumulator = 0
clean = True

for index in changeList:
    clean = True
    for key in lineCount:
        lineCount[key] = 0
    accumulator = 0
    i = 0
    while i < len(instructions):
        currentInstruction = instructions[i]
        if i == index:
            if 'nop' in currentInstruction:
                currentInstruction = currentInstruction.replace('nop', 'jmp')
            if 'jmp' in currentInstruction:
                currentInstruction = currentInstruction.replace('jmp', 'nop')

        if lineCount[i] == 1:
            # break, loop detection
            #print("Aborting infinite loop.")
            #print("This instruction will be executed a second time: " + currentInstruction)
            #print("Current instruction number: " + str(i))
            #print("Accumulator: " + str(accumulator))
            clean = False
            break

        lineCount[i] += 1

        if 'acc' in currentInstruction:
            instrSplit = currentInstruction.split(' ')
            accumulator += int(instrSplit[1])
            i += 1

        if 'nop' in currentInstruction:
            i += 1

        if 'jmp' in currentInstruction:
            instrSplit = currentInstruction.split(' ')
            jump = int(instrSplit[1])
            i += jump
    if clean:
        cleanAccumulator = accumulator
        break


if clean:
    print("Infinity loop solved.")
    print("Accumulator: " + str(cleanAccumulator))
