commands = []
with open("C:\\Privat\\advent_of_code20\\puzzle12\\input1.txt") as f:
    for line in f:
        line = line.strip()
        commands.append(line)

print(commands)

root = (0,0)
newPosition = (0,0) # (x, y)
waypoint = (10, 1)
direction = 90 # N = 0, E = 90, S = 180, W = 270
print("Position: " + str(newPosition) + " | Direction: " + str(direction))
for command in commands:
    value = int(command[1:])
    newDirection = direction
    changedWaypoint = waypoint
    if 'N' in command:
        changedWaypoint = (waypoint[0], waypoint[1] + value)

    if 'S' in command:
        changedWaypoint = (waypoint[0], waypoint[1] - value)

    if 'E' in command:
        changedWaypoint = (waypoint[0] + value, waypoint[1])

    if 'W' in command:
        changedWaypoint = (waypoint[0] - value, waypoint[1])

    if 'L' in command:
        if value == 90:
            changedWaypoint = (-1 * waypoint[1], waypoint[0])
        if value == 180:
            changedWaypoint = (-1 * waypoint[0], -1 * waypoint[1])
        if value == 270:
            changedWaypoint = (waypoint[1], -1 * waypoint[0])

        print("Command: " + command + " | Old waypoint: " + str(waypoint) + " | new waypoint: " + str(changedWaypoint))

    if 'R' in command:
        if value == 90:
            changedWaypoint = (waypoint[1], -waypoint[0])
        if value == 180:
            changedWaypoint = (-waypoint[0], -waypoint[1])
        if value == 270:
            changedWaypoint = (-waypoint[1], waypoint[0])

        print("Command: " + command + " | Old waypoint: " + str(waypoint) + " | new waypoint: " + str(changedWaypoint))

    if 'F' in command:
        changedPosition = (newPosition[0] + value * waypoint[0], newPosition[1] + value * waypoint[1])

    direction = newDirection
    newPosition = changedPosition
    waypoint = changedWaypoint
    #print("Command: " + command + " | Position: " + str(newPosition) + " | Direction: " + str(direction))

#manhattan distance

dist = abs(root[0] - newPosition[0]) + abs(root[1] - newPosition[1])
print("Manhattan distance to new position: " + str(dist))
