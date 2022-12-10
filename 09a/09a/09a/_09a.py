import math

# (x, y)
fContent = open("input.txt", "r").readlines()

def dist(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def moveH(h, direction):  
    if direction == "R": return add(h, (1, 0))
    elif direction == "L": return add(h, (-1, 0))
    elif direction == "U": return add(h, (0, -1))
    else: return add(h, (0, 1))

def moveT(h, t, direction):
    if direction == "R": return (h[0] - 1, h[1])
    elif direction == "L": return (h[0] + 1, h[1])
    elif direction == "U": return (h[0], h[1]  + 1)
    else: return (h[0], h[1] - 1)
    
h = (0, 0)
t = (0, 0)
fields = []
for line in fContent:
    directory, length = line.strip().split(" ")
    #print(h, "-----------", line.strip())
    for i in range(0, int(length)):
        h = moveH(h, directory)
        distance = dist(h, t)
        if distance >= 2:
            t = moveT(h, t, directory)
            fields.append(t)
        #print("h:", h, "t:", t, "dist:", d)


print("Positions visited by tail of the rope: ", len(dict.fromkeys(fields)) + 1)