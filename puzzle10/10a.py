jolts = []

with open("C:\\Privat\\advent_of_code20\\puzzle10\\input1.txt") as f:
    for line in f:
        line = line.strip()
        jolts.append(int(line))

jolts = sorted(jolts)

print(jolts)

countOne = 0
countThree = 0

i = 1
while i < len(jolts):
    diff = jolts[i] - jolts[i - 1]
    if diff == 1:
        countOne += 1
    if diff == 3:
        countThree += 1

    i += 1

if jolts[0] == 1:
    countOne += 1

countThree += 1 #built-in adapter

print(countOne)
print(countThree)

print("Multiplication of differences: " + str(countOne) + "(1-jolt) * " + str(countThree) + " (3-jolt) = " + str(countOne * countThree))
