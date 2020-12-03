items = []

with open("C:\\Privat\\advent_of_code20\\puzzle1\\input1.txt") as f:
    for line in f:
        items.append(int(line))

expenses = 0

for item in items:
    #print(str(item))
    for item2 in items:
        for item3 in items:
            sum = item + item2 + item3
            #print(str(item) + " + " + str(item2) + " = " + str(sum))
            if sum == 2020:
                expenses = item * item2 * item3
                print("Fix the expense report: " + str(item) + " * " + str(item2) + " * " + str(item3) + " = " + str(expenses))
