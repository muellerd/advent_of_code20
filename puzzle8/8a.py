accumulator = 0

instructions = []
lineCount = {}

with open("C:\\Privat\\advent_of_code20\\puzzle8\\input1.txt") as f:
    i = 0
    for line in f:
        line = line.strip()
        instructions.append(line)
        lineCount[i] = 0
        i += 1

print(instructions)
print(lineCount)

i = 0
while i < len(instructions):
    currentInstruction = instructions[i]
    print(currentInstruction)

    if lineCount[i] == 1:
        # break, loop detection
        print("Aborting infinite loop.")
        print("This instruction will be executed a second time: " + currentInstruction)
        print("Current instruction number: " + str(i))
        print("Accumulator: " + str(accumulator))
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

print(lineCount)
