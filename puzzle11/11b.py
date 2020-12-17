class Seating:
    def __init__(self, gen):
        self.seats = []
        self.generation = gen

    def __str__(self):
        countOccupied = 0
        for seatRow in self.seats:
            for seat in seatRow:
                if seat == '#':
                    countOccupied += 1
        return "Seating gen-" + str(self.generation) + ": " + str(countOccupied) + " seats are occupied"

    def printSeating(self):
        print('------')
        print(self)
        for seatRow in self.seats:
            str = ''
            for seat in seatRow:
                str += seat
            print(str)

def areSeatingsEqual(firstSeating: Seating, secondSeating: Seating):
    equal = True
    for i in range(0, len(firstSeating.seats)):
        for j in range(0, len(firstSeating.seats[i])):
            equal = equal and firstSeating.seats[i][j] == secondSeating.seats[i][j]
            if not equal:
                break
        if not equal:
            break
    return equal

def deepCopy(seating: Seating):
    seats = []
    for i in range(0, len(seating.seats)):
        row = []
        for j in range(0, len(seating.seats[i])):
            row.append(seating.seats[i][j])
        seats.append(row)
    return seats

seatInput = []
with open("C:\\Privat\\advent_of_code20\\puzzle11\\input1.txt") as f:
    for line in f:
        line = line.strip()
        seatInput.append(list(line))

firstSeating = Seating(0)
firstSeating.seats = seatInput

firstSeating.printSeating()
stable = False

currentSeating = firstSeating
while not stable:
    # create next generation
    nextSeating = Seating(currentSeating.generation + 1)
    nextSeating.seats = deepCopy(currentSeating)
    for i in range(0, len(currentSeating.seats)):
        for j in range(0, len(currentSeating.seats[i])):
            symbol = currentSeating.seats[i][j]
            if symbol == '.':
                continue
            # check adjacent seats -> number of occupied seats
            occupied = 0
            # top left
            row = i - 1
            col = j - 1
            while row >= 0 and col >= 0:
                topLeft = currentSeating.seats[row][col]
                if topLeft == '#':
                    occupied += 1
                if topLeft != '.':
                    break
                row -= 1
                col -= 1

            # top
            row = i - 1
            col = j
            while row >= 0:
                top = currentSeating.seats[row][col]
                if top == '#':
                    occupied += 1
                if top != '.':
                    break
                row -= 1

            # top right
            row = i - 1
            col = j + 1
            while row >= 0 and col < len(currentSeating.seats[row]):
                topRight = currentSeating.seats[row][col]
                if topRight == '#':
                    occupied += 1
                if topRight != '.':
                    break
                row -= 1
                col += 1

            # left
            row = i
            col = j - 1
            while col >= 0:
                left = currentSeating.seats[row][col]
                if left == '#':
                    occupied += 1
                if left != '.':
                    break
                col -= 1

            # right
            row = i
            col = j + 1
            while col < len(currentSeating.seats[row]):
                right = currentSeating.seats[row][col]
                if right == '#':
                    occupied += 1
                if right != '.':
                    break
                col += 1

            # bottom left
            row = i + 1
            col = j - 1
            while col >= 0 and row < len(currentSeating.seats):
                bottomLeft = currentSeating.seats[row][col]
                if bottomLeft == '#':
                    occupied += 1
                if bottomLeft != '.':
                    break
                row += 1
                col -= 1

            # bottom
            row = i + 1
            col = j
            while row < len(currentSeating.seats):
                bottom = currentSeating.seats[row][col]
                if bottom == '#':
                    occupied += 1
                if bottom != '.':
                    break
                row += 1

            # bottom right
            row = i + 1
            col = j + 1
            while row < len(currentSeating.seats) and col < len(currentSeating.seats[row]):
                bottomRight = currentSeating.seats[row][col]
                if bottomRight == '#':
                    occupied += 1
                if bottomRight != '.':
                    break
                row += 1
                col += 1

            if symbol == 'L' and occupied == 0:
                nextSeating.seats[i][j] = '#'
            if symbol == '#' and occupied >= 5:
                nextSeating.seats[i][j] = 'L'

    equal = areSeatingsEqual(currentSeating, nextSeating)
    nextSeating.printSeating()
    if equal:
        stable = True
    else:
        currentSeating = nextSeating

print(currentSeating)
