import re

def p(mp):
    for r in mp:
        for c in r:
            print(c, end="")
        print("")
    print("-------------------------------------")

def setDirection(direction, change):
    if change == "R": 
        direction += 1
        if direction == 4: direction = 0
    elif change == "L": 
        direction -= 1
        if direction == -1: direction = 3
    return direction

def splitInstruction(ins):
    s = 0
    d = None
    if ins.isdigit():
        s = int(ins)
    else:
        s = int(ins[1:])
        d = ins[0]

    return (s, d)

def readData(fileName):
    mp = []
    insText = ""

    with open(fileName,"r") as fContent:
        storeInstruction = False
        for line in fContent.readlines():
            if line == "\n": storeInstruction = True
            if storeInstruction: insText += line.rstrip()
            else: mp.append([x for x in line.rstrip()])
    return (mp, insText)

size = 4                # testInput=4, input=50
data = readData("testinput.txt")
mp = data[0]
cPos = (0, size * 2)    # (y, x)
direction = 0           # R-0, D-1, L-2, U-3
c = [">", "v", "<", "^"]

for instructionText in re.findall(r"[R|L]?[\d]+", data[1].strip()):
    ins = splitInstruction(instructionText)
    
    y = cPos[0]
    x = cPos[1]
    direction = setDirection(direction, ins[1])

    for i in range(0, ins[0] + 1):
        match direction:
            case 0:
                if i != 0:
                    # 1 -> 6
                    if (0 <= y < size) and ((x + 1) == (size * 3)):
                        y = (size * 3) - 1 - y
                        x = (size * 4) - 1
                        direction = 2
                    # 4 -> 6
                    elif (size <= y < (size * 2)) and ((x + 1) == (size * 3)):                      
                        x = ((size * 4) - 1) - (y - size)
                        y = (size * 2)
                        direction = 1
                    # 6 -> 1
                    elif ((size * 2) <= y < (size * 3)) and ((x + 1) == (size * 4)):
                        y = (size * 3) - 1 - y
                        x = (size * 3) - 1
                        direction = 2
                    # Rest
                    else: x += 1
            case 1:
                if i != 0:
                    # 2 -> 5
                    if ((y + 1) == (size * 2)) and (0 <= x < size):
                        y = (size * 3) - 1
                        x = (size * 3) - 1 - x
                        direction = 3
                    # 3 -> 5
                    elif ((y + 1) == (size * 2)) and (size <= x < (size * 2)):
                        y = (size * 3) - 1 + (size - x)
                        x = (size * 2)
                        direction = 0
                    # 5 -> 2
                    elif ((y + 1) == (size * 3)) and ((size * 2) <= x < (size * 3)):
                        y = (size * 2) - 1
                        x = (size * 3) - 1 - x
                        direction = 3
                    # 6 -> 2
                    elif ((y + 1) == (size * 4)) and ((size * 3) <= x < (size * 4)):
                        y = (size * 3) - 1 + ((size * 2) - x)
                        x = 0
                        direction = 0
                    # Rest
                    else: y += 1
            case 2:
                if i != 0:
                    # 1 -> 3
                    if (0 <= y < size) and x == (size * 2):
                        x = size + y
                        y = size
                        direction = 1
                    # 2 -> 6
                    elif (size <= y < (size * 2)) and x == 0:
                        x = (size * 3) - 1 + ((size * 2) - y)
                        y = (size * 3) - 1
                        direction = 3
                    # 5 -> 3
                    elif ((size * 2) <= y < (size * 3)) and (x == (size * 2)):
                        x = (size * 2) - 1 + ((size * 2) - y)
                        y = (size * 2) - 1
                        direction = 3
                    # Rest
                    else: x -= 1
            case 3:
                if i != 0:
                    # 1 -> 2
                    if y == 0 and ((size * 2) <= x < (size * 3)):
                        x = (size * 3) - 1 - x
                        y = size
                        direction = 1
                    # 2 -> 1
                    elif y == size and (0 <= x < size):
                        y = 0
                        x = (size * 3) - 1 - x
                        direction = 1
                    # 3 -> 1
                    elif y == size and (size <= x < (size * 2)):
                        y = x - size
                        x = size * 2
                        direction = 0
                    # 6 -> 4
                    elif y == (size * 2) and ((size * 3) <= x < (size * 4)):
                        y = size + (size * 2) - x
                        x = (size * 3) - 1
                        direction = 2
                    else: y -= 1
        
        if mp[y][x] == "#":
            break

        cPos = (y, x)
        mp[y][x] = c[direction]
    #p(mp)

p(mp)
passwordValue = (1000 * (cPos[0] + 1)) + (4 * (cPos[1] + 1)) + c.index((mp[cPos[0]][cPos[1]]))
print(f"Final password: 1000 * {cPos[0] + 1} + 4 * {cPos[1] + 1} + {(mp[cPos[0]][cPos[1]])} = {passwordValue}")