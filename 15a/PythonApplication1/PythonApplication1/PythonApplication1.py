import re
import numpy as np
import math

def flatten(array):
    newArr = []
    for arr in array:
        for aa in arr:
            newArr.append(aa)
    return newArr

def read(fileName):
    with open(fileName, "r") as fContent:
        pairs = []

        for line in fContent.readlines():
            sX, sY, bX, bY = map(int, re.findall(f"[+-]?\d+", line.strip()))
            sbDist = abs(sY - bY) + abs(sX - bX)                                # sensor-beacon distance
            pairs.append([[sY, sX], [bY, bX], sbDist])

        return pairs
    
data = read("testinput.txt")
xs = np.array([[el[0][1], el[1][1]] for el in data]).flatten()
minX = min(xs)
maxX = max(xs)
width = maxX - minX
y = 11   

arr = ["#"] * width
#mark beacons and sensons
for sb in data:
    if sb[1][0] == y:
        arr[abs(minX) + sb[1][1]] = "B"
        break
    if sb[0][0] == y:
        arr[abs(minX) + sb[0][1]] = "S"
        break

for x in range(minX, width + minX):
    inRange = False
    
    for sb in data:
        sbDist = sb[2]
        sxDist = abs(sb[0][0] - y) + abs(sb[0][1] - x)                      # sensor-(x, y) distance

        if sbDist >= sxDist: 
            inRange = True
            break
    
    if not inRange:
        arr[x - minX] = "."

count = 0 
for a in arr:
    if a == "#":
        count+=1
print(arr)
print(f"In the row where y={y}, {count} positions cannot contain a beacon ")
# 3876819