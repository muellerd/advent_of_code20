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
            if i-1 >= 0 and j-1 >= 0:
                topLeft = currentSeating.seats[i-1][j-1]
                if topLeft == '#':
                    occupied += 1
            if i-1 >= 0:
                top = currentSeating.seats[i-1][j]
                if top == '#':
                    occupied += 1
            if i-1 >= 0 and j+1 < len(currentSeating.seats[i]):
                topRight = currentSeating.seats[i-1][j+1]
                if topRight == '#':
                    occupied += 1
            if j-1 >= 0:
                left = currentSeating.seats[i][j-1]
                if left == '#':
                    occupied += 1
            if j+1 < len(currentSeating.seats[i]):
                right = currentSeating.seats[i][j+1]
                if right == '#':
                    occupied += 1
            if i+1 < len(currentSeating.seats) and j-1 >= 0:
                bottomLeft = currentSeating.seats[i+1][j-1]
                if bottomLeft == '#':
                    occupied += 1
            if i+1 < len(currentSeating.seats):
                bottom = currentSeating.seats[i+1][j]
                if bottom == '#':
                    occupied += 1
            if i+1 < len(currentSeating.seats) and j+1 < len(currentSeating.seats[i]):
                bottomRight = currentSeating.seats[i+1][j+1]
                if bottomRight == '#':
                    occupied += 1

            if symbol == 'L' and occupied == 0:
                nextSeating.seats[i][j] = '#'
            if symbol == '#' and occupied >= 4:
                nextSeating.seats[i][j] = 'L'

    equal = areSeatingsEqual(currentSeating, nextSeating)
    nextSeating.printSeating()
    if equal:
        stable = True
    else:
        currentSeating = nextSeating

print(currentSeating)
