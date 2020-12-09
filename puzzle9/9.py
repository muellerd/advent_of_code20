numbers = []

with open("C:\\Privat\\advent_of_code20\\puzzle9\\input1.txt") as f:
    for line in f:
        line = line.strip()
        numbers.append(int(line))

print(numbers)

#preamble = 5    #example
preamble = 25  #input

invalidNumber = None

i = preamble
while i < len(numbers):

    found = False
    # check whether this number can be built by two numbers of the previous indices
    for j in range(i-preamble, i-1):
        for k in range(i-preamble+1,i):
            sum = int(numbers[j]) + int(numbers[k])
            if sum == int(numbers[i]):
                found = True
                print("Checking number: " + str(numbers[i]) + " -> " + str(numbers[j]) + " + " + str(numbers[k]) + " = " + str(sum) + " => " + str(found))

    if not found:
        print("No valid combination for number " + str(numbers[i]))
        invalidNumber = int(numbers[i])
        break

    i += 1

i = 0
while i < len(numbers):

    minNumber = numbers[i]
    maxNumber = numbers[i]
    sum = numbers[i]

    j = i + 1
    while j < len(numbers):
        if numbers[j] < minNumber:
            minNumber = numbers[j]
        if numbers[j] > maxNumber:
            maxNumber = numbers[j]

        sum += numbers[j]

        if sum >= invalidNumber:
            break

        j += 1

    if sum == invalidNumber:
        print("Min number: " + str(minNumber))
        print("Max number: " + str(maxNumber))
        print("Sum: " + str(minNumber + maxNumber))
        break

    i += 1
