commands = []
with open("C:\\Privat\\advent_of_code20\\puzzle12\\input1.txt") as f:
    for line in f:
        line = line.strip()
        commands.append(line)

print(commands)

root = (0,0)
newPosition = (0,0) # (x, y)
direction = 90 # N = 0, E = 90, S = 180, W = 270
print("Position: " + str(newPosition) + " | Direction: " + str(direction))
for command in commands:
    value = int(command[1:])
    newDirection = direction
    if 'N' in command:
        changedPosition = (newPosition[0], newPosition[1] + value)

    if 'S' in command:
        changedPosition = (newPosition[0], newPosition[1] - value)

    if 'E' in command:
        changedPosition = (newPosition[0] + value, newPosition[1])

    if 'W' in command:
        changedPosition = (newPosition[0] - value, newPosition[1])

    if 'L' in command:
        newDirection = direction - value
        if newDirection < 0:
            newDirection = 360 + newDirection
        if newDirection >= 360:
            newDirection -= 360

    if 'R' in command:
        newDirection = direction + value
        if newDirection >= 360:
            newDirection -= 360

    if 'F' in command:
        if direction == 0:
            changedPosition = (newPosition[0], newPosition[1] + value)
        if direction == 90:
            changedPosition = (newPosition[0] + value, newPosition[1])
        if direction == 180:
            changedPosition = (newPosition[0], newPosition[1] - value)
        if direction == 270:
            changedPosition = (newPosition[0] - value, newPosition[1])

    direction = newDirection
    newPosition = changedPosition
    #print("Command: " + command + " | Position: " + str(newPosition) + " | Direction: " + str(direction))

#manhattan distance

dist = abs(root[0] - newPosition[0]) + abs(root[1] - newPosition[1])
print("Manhattan distance to new position: " + str(dist))
