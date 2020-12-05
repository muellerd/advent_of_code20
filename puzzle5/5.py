import math

# 128 rows, numbered 0 - 127
# 8 columns, numbered 0 - 7
# example: FBFBBFFRLR

minRow = 0
lastRow = 127
minColumn = 0
lastColumn = 7

highestSeatId = 0

ids = []
seatDict = {}

with open("C:\\Privat\\advent_of_code20\\puzzle5\\input1.txt") as f:
    for line in f:
        line = line.strip()

        rows = list(range(0, 128))
        columns = list(range(0, 8))

        rowLine = line[:-3]
        columnLine = line[7:]

        for char in rowLine:
            newRows = rows
            if char == 'F':
                newRows = rows[:int(len(rows) / 2)]

            if char == 'B':
                newRows = rows[int(len(rows) / 2):]

            rows = newRows

        for char in columnLine:
            newColumns = columns
            if char == 'L':
                newColumns = columns[:int(len(columns) / 2)]

            if char == 'R':
                newColumns = columns[int(len(columns) / 2):]

            columns = newColumns

        seatId = rows[0] * 8 + columns[0]
        ids.append(seatId)
        if not rows[0] in seatDict:
            seatDict[rows[0]] = []
        seatDict[rows[0]].append(columns[0])
        if seatId > highestSeatId:
            highestSeatId = seatId

        print(line + ": row=" + str(rows[0]) + ", column=" + str(columns[0]) + " seatid=" + str(seatId))

print("Highest seat id: " + str(highestSeatId))
print(sorted(ids))
for key in seatDict:
    seatDict[key] = sorted(seatDict[key])

missingSeats = []

for key in sorted(seatDict):
    if len(seatDict[key]) < 8:
        print(str(key) + ": " + str(seatDict[key]))
        for i in range(0, 8):
            if not i in seatDict[key]:
                missingSeats.append((key, i))

print("Missing seats: " +str(missingSeats))
for missingSeat in missingSeats:
    sid = missingSeat[0] * 8 + missingSeat[1]
    if (sid + 1) in ids and (sid - 1) in ids:
        print("Your seat ID: " + str(sid))




