import timeit

start = timeit.default_timer()

jolts = []

class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data

    def __str__(self):
        return "Tree '" + str(self.data) + "': " + str(self.children)

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

joltToPossibleJolts = {}
for jolt in jolts:
    if not jolt in joltToPossibleJolts:
        joltToPossibleJolts[jolt] = []
    for j in jolts:
        if j > jolt and j <= jolt + 3:
            joltToPossibleJolts[jolt].append(j)

root = Tree(0)

print(root)

leaves = []
leaves.append(root)

while len(leaves) > 0:
    toAppend = []
    toRemove = []
    for leaf in leaves:
        for jolt in joltToPossibleJolts[leaf.data]:
            t = Tree(jolt)
            leaf.children.append(t)
            if not leaf in toRemove:
                toRemove.append(leaf)
            toAppend.append(t)

    #clean up
    for leaf in toRemove:
        leaves.remove(leaf)
    for leaf in toAppend:
        leaves.append(leaf)

    countLastLeaf = 0
    for leaf in leaves:
        if leaf.data == maxJolt + 3:
            countLastLeaf += 1

    stop = timeit.default_timer()
    print('Time: ', round(stop - start, 2), ' seconds')
    print('Number of open leaves: ' + str(len(leaves) - countLastLeaf))

    if countLastLeaf == len(leaves):
        break

print("Number of remaining leaves: " + str(len(leaves)))


stop = timeit.default_timer()

print('Time: ', round(stop - start, 2), ' seconds')
