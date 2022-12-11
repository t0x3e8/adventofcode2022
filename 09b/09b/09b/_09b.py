import math
import numpy as np

# (x, y)
fContent = open("testinput.txt", "r").readlines()

def dist(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def calc(p1, p2, d):
    # U D
    if d[0] == 0:
        diff = abs(p1[0]) - abs(p2[0])
        if (p1[0] >= 0):
            p1 = (p1[0] - np.sign(diff), p1[1] + np.sign(d[1]))
        if (p1[0] <= 0):
            p1 = (p1[0] + np.sign(diff), p1[1] - np.sign(d[1]))
    # L R
    if d[1] == 0:
        diff = abs(p1[1]) - abs(p2[1])
        if (p1[1] >= 0):
            p1 = (p1[0] + np.sign(d[0]), p1[1] - np.sign(diff))  
        if (p1[1] < 0):
            p1 = (p1[0] - np.sign(d[0]), p1[1] + np.sign(diff))
        

    return p1


directions = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
ropes = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
fields = []
for line in fContent:
    d, length = line.strip().split(" ")
    print(ropes[0], "-----------", line.strip())
        
    for i in range(int(length)):
        ropes[0] = add(ropes[0], directions[d])
        print(f"--> 0: {ropes[0]}")

        for ropeIndex in range(1, len(ropes)):
            rng = dist(ropes[ropeIndex], ropes[ropeIndex - 1])
            if rng >= 2:
                s = (f"{ropeIndex}: OLD {ropes[ropeIndex]}, DIR: {directions[d]}, DIFF: ({ropes[ropeIndex][0] - ropes[ropeIndex - 1][0]}, {ropes[ropeIndex][1] - ropes[ropeIndex - 1][1]})")
                ropes[ropeIndex] = calc(ropes[ropeIndex], ropes[ropeIndex - 1], directions[d])
                fields.append(ropes[ropeIndex])                
                print(s + " NEW: ", ropes[ropeIndex])
            else:
                print(f"    {ropeIndex}: {ropes[ropeIndex]}")

print("Positions visited by tail of the 9 ropes: ", len(dict.fromkeys(fields)) + 1)
#2471
