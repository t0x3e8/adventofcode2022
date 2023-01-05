import re
import numpy as np
import time

def read(fileName):
    with open(fileName, "r") as fContent:
        pairs = []

        for line in fContent.readlines():
            sX, sY, bX, bY = map(int, re.findall(f"[+-]?\d+", line.strip()))
            sbDist = abs(sY - bY) + abs(sX - bX)                                # sensor-beacon distance
            pairs.append([[sY, sX], [bY, bX], sbDist])

        return pairs
    
def markUsedPosition(data):
    arr = []
    #mark beacons and sensons
    for sb in data:
        arr.append((sb[0][1], sb[0][0]))
        arr.append((sb[1][1], sb[1][0]))
    return arr

data = read("testinput.txt")
#maxy = 4000000
maxy = 20
#maxy = 10000

sTime = time.time()
usedPositions = markUsedPosition(data)
eTime = time.time()
print(f"Marking B and S time: {(eTime-sTime):.5f}")

sTime = time.time()
for x in range(maxy):
    for y in range(maxy):
        if (y, x) in usedPositions:
            continue

        breaker = False

        for sb in data:
            sbDist = sb[2]
            sxDist = abs(sb[0][0] - y) + abs(sb[0][1] - x)

            if sbDist >= sxDist:
                breaker = True
                break
        if not breaker:
            print(f"({y}, {x}) => {(maxy * x) + y}")
    
        
eTime = time.time()
print(f"Calculating used positions time: {(eTime-sTime):.5f}")
# 12567351400528
