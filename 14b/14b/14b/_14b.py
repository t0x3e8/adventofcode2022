
import re
import numpy as np
fContent = open("testinput.txt", "r").read()


#b = np.eye(10)
#c = np.empty((10, 1))
#b = np.insert(b, 0, c, axis=1)

def ppp(b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            print(b[i][j], " ", end="")
        print("")


pairs = re.findall(r"(\d+,\d+)", fContent, re.DOTALL)
xSet = [int(x.split(",")[0]) for x in pairs]
ySet = [int(x.split(",")[1]) for x in pairs]
shape = (max(ySet) + 1, max(xSet) - min(xSet) + 1)
cave = np.full(shape, ".")
cave[0, 500 - min(xSet)] = "+"

offset = (min(xSet), min(ySet))
for line in fContent.split("\n"):
    pairs2 = re.findall(r"(\d+,\d+)+", line, re.DOTALL)
    for i in range(len(pairs2)):
        if i + 1 == len(pairs2): break
        pCur = pairs2[i].split(",")
        pNext = pairs2[i + 1].split(",")
        for x in range(min(int(pCur[0]), int(pNext[0])), max(int(pCur[0]), int(pNext[0])) + 1):
            for y in range(min(int(pCur[1]), int(pNext[1])), max(int(pCur[1]), int(pNext[1])) + 1):
                cave[y][x-offset[0]] = "#"

sand = (1, 500 - min(xSet))
x = 0
y = 1
while True:
    ppp(cave)
    print(x)
    if (sand[1] + x) < 0:
        newC = np.ones((1, max(ySet) + 1))
        cave = np.insert(cave, 0, newC, axis = 1)
        cave[len(cave) - 1][0] = "#"
        x = 0 
        y = 1
    if (sand[1] + x) >= len(cave[0]):
        newC = np.ones((1, max(ySet) + 1))
        cave = np.insert(cave, len(cave[0]), newC, axis = 1)
        cave[len(cave) - 1][max(ySet) + 1] = "#"
        x = 0 
        y = 1
    field = cave[sand[0] + y][sand[1] + x]
    if field == ".":
        y += 1
    else:
        x -= 1
        field = cave[sand[0] + y][sand[1] + x]
        if not field == ".":
            x += 2
            field = cave[sand[0] + y][sand[1] + x]
            if not field == ".":
                cave[sand[0] + y - 1][sand[1] + x - 1] = "o"
                x = 0
                y = 1
                                
print("Total number of 'o' is: ", np.count_nonzero(cave == "o"))