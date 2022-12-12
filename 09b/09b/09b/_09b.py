import math
import numpy as np

fContent = open("input.txt", "r").readlines()
directions = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
ropes = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
fields = [[], [], [], [], [], [], [], [], []]

def dist(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def calc(p1, p2):
    diff = (p1[0] - p2[0], p1[1] - p2[1])
    return (p1[0] - np.sign(diff[0]), p1[1] - np.sign(diff[1]))

for line in fContent:
    d, length = line.strip().split(" ")
        
    for i in range(int(length)):
        ropes[0] = (ropes[0][0] + directions[d][0], ropes[0][1] + directions[d][1])

        for ropeIndex in range(1, len(ropes)):
            rng = dist(ropes[ropeIndex], ropes[ropeIndex - 1])
            if rng >= 2 :
                ropes[ropeIndex] = calc(ropes[ropeIndex], ropes[ropeIndex - 1])
                fields[ropeIndex - 1].append(ropes[ropeIndex])

for i in range(9):
    print(f"Positions visited the tail of {i} rope: ", len(dict.fromkeys(fields[i])) + 1)