import re
import numpy as np
import math
import time

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
xs = np.array([[el[0][1] - el[2], el[1][1], el[0][1] + el[2]] for el in data]).flatten()
minX = min(xs)
maxX = max(xs)
width = maxX - minX
#y = 11
y = 2000000

sTime = time.time()
arr = ["#"] * width
usedPositions = []
#mark beacons and sensons
for sb in data:
    if sb[1][0] == y or sb[0][0] == y:
        usedPositions.append(abs(minX) + sb[1][1])
        break
eTime = time.time()
print(f"Marking B and S time: {(eTime-sTime):.5f}")

sTime = time.time()
for x in range(minX, width + minX):
    inRange = False
    
    for sb in data:
        sbDist = sb[2]
        sxDist = abs(sb[0][0] - y) + abs(sb[0][1] - x)   # sensor-(x, y) distance

        if sbDist >= sxDist: 
            inRange = True
            break
    
    if not inRange:
        arr[x - minX] = "."
        
eTime = time.time()
print(f"Calculating used positions time: {(eTime-sTime):.5f}")

sTime = time.time()
count = 0 
for a in arr:
    if a == "#":
        count+=1
eTime = time.time()
print(f"Counting time: {(eTime-sTime):.5f}")
print(f"In the row where y={y}, {count} positions cannot contain a beacon ")
# 6078701