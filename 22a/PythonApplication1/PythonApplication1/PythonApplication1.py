import re

def findY(mp, col, fromBottom):
    for r in range(len(mp)):
        if fromBottom:
            rowFromBottom = len(mp) - r - 1
            if len(mp[rowFromBottom]) > col and mp[rowFromBottom][col] != " ": return rowFromBottom
        else:
            if mp[r][col] != " ": return r

def findX(mp, row, fromRight):
    for i in range(len(mp[row])):
        if fromRight:
            colFromRight = len(mp[row]) - i - 1
            if mp[row][colFromRight] != " ": return colFromRight
        else:
            if (mp[row][i]) != " ": return i

def p(mp):
    for r in mp:
        for c in r:
            print(c, end="")
        print("")
    print("-------------------------------------")

def changeDirection(direction, change):
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

def readData():
    mp = []
    insText = ""

    with open("input.txt","r") as fContent:
        storeInstruction = False
        for line in fContent.readlines():
            if line == "\n":storeInstruction = True
            if storeInstruction: insText += line.rstrip()
            else: mp.append([x for x in line.rstrip()])
    return (mp, insText)

data = readData()
mp = data[0]
sPos = (0, mp[0].index(".")) #(y, x)
direction = 0 # 0 R, 1 D, 2 L, 3 U

a = findX(mp, 1, False)

prevInstruction = ""
for instruction in re.findall(r"[R|L]?[\d]+", data[1].strip()):
    ins = splitInstruction(instruction)
    if instruction == "R28" and prevInstruction == "R35":
        prevInstruction = instruction
    
    prevInstruction = instruction
    y = sPos[0]
    x = sPos[1]
    c = ""
    direction = changeDirection(direction, ins[1])

    for i in range(0, ins[0] + 1):
        match direction:
            case 0:
                c = ">"
                if i != 0:
                    if (x + 1) >= len(mp[y]) or mp[y][x] == " ":
                        x = findX(mp, y, False)
                    else: x += 1
            case 1:
                c = "v"
                if i != 0:
                    if (y + 1) >= len(mp) or x >= len(mp[y + 1]) or mp[y][x] == " ":
                        y = findY(mp, x, False)
                    else: y += 1
            case 2:
                c = "<"
                if i != 0:
                    if (x - 1) < 0 or mp[y][x - 1] == " ":
                        x = findX(mp, y, True) 
                    else: x -= 1
            case 3:
                c = "^"
                if i != 0:
                    if (y - 1) < 0 or mp[y - 1][x] == " ":
                        y = findY(mp, x, True)      
                    else: y -= 1
        if mp[y][x] == "#":
            break

        sPos = (y, x)
        mp[y][x] = c

p(mp)
passwordValue = (1000 * (sPos[0] + 1)) + (4 * (sPos[1] + 1)) + direction
print(f"Final password: 1000 * {sPos[0] + 1} + 4 * {sPos[1] + 1} + {direction} = {passwordValue}")