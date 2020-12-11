jolts = []
maxJolt = 0

with open("C:\\Privat\\advent_of_code20\\puzzle10\\input1.txt") as f:
    for line in f:
        line = line.strip()
        jolts.append(int(line))
        if int(line) > maxJolt:
            maxJolt = int(line)

jolts.append(0)
jolts.append(maxJolt + 3)

jolts = sorted(jolts)

pathsToJolt = {}
pathsToJolt[0] = 1
i = 0
while i < len(jolts):
    for j in range(1,4):
        if i + j < len(jolts) and jolts[i + j] - jolts[i] <= 3:
            if not jolts[i + j] in pathsToJolt:
                pathsToJolt[jolts[i + j]] = 0
            pathsToJolt[jolts[i + j]] += pathsToJolt[jolts[i]]

    i += 1

print("Distinct ways to arrange the adapters: " + str(pathsToJolt[maxJolt + 3]))
