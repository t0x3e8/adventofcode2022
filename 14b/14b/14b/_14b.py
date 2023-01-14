import re
import numpy as np
fContent = open("input.txt", "r").read()

def printCave(cave):
    for l in cave:
        print("".join(l))

pairs = re.findall(r"(\d+,\d+)", fContent, re.DOTALL)
xSet = [int(x.split(",")[0]) for x in pairs]
ySet = [int(x.split(",")[1]) for x in pairs]
shape = (max(ySet) + 3, 2 * (max(ySet) + 3) + 1)
cave = np.full(shape, ".")
cave[0][int(shape[1] / 2)] = "+"
cave[shape[0] - 1] = "#" * shape[1]

for line in fContent.split("\n"):
    pairs2 = re.findall(r"(\d+,\d+)+", line, re.DOTALL)
    for i in range(len(pairs2)):
        if i + 1 == len(pairs2): break
        pCur = pairs2[i].split(",")
        pNext = pairs2[i + 1].split(",")
        for x in range(min(int(pCur[0]), int(pNext[0])), max(int(pCur[0]), int(pNext[0])) + 1):
            for y in range(min(int(pCur[1]), int(pNext[1])), max(int(pCur[1]), int(pNext[1])) + 1):
                offset = x - 500 + int(shape[1] / 2)
                cave[y][offset] = "#"

sand = (0, int(shape[1] / 2))
x, y = (0, 0)

while True:
    for yy, xx in [(1, 0), (1, -1), (1, 1)]:
            if cave[sand[0] + y + yy][sand[1] + x + xx] == ".":
                y += yy
                x += xx
                break
    else:
        cave[sand[0] + y][sand[1] + x] = "O"
        if x == 0 and y == 0:
            break
        x, y = (0, 0)

printCave(cave)
print("Total number of 'O' is: ", np.count_nonzero(cave == "O"))