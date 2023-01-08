import re

def readInput(filename):
    with open(filename, "r") as fContent:
        data = []
        for line in fContent.readlines():
            r = re.findall(r"([A-Z]{2})", line)
            data.append({"key": r[0], "rate": int(re.findall(r"[\d]+", line)[0]), "children": r[1:] })
        return data

data = readInput("testinput.txt")
curPressure = 0
totalPressure = 0
valve = data[0]
openValves = []

isMoving = False
isOpening = False
for m in range (1, 31):
    print(f"== Minute {m} ==")
    if len(openValves):
        print(f"Valve {openValves} is open, releasing {valve['rate']} pressure.")
    else:
        print("No valves are open.")

    if not isMoving and not isOpening:
        for v in valve["children"]:
            if v not in openValves:
                valve = next(d for d in data if d["key"] == v)
                print(f"You move to valve {v}.")
                isMoving = True
                break
    elif isMoving and not isOpening:
        print(f"You open valve {valve['key']}.")
        isMoving = False
        if valve["key"] not in openValves:
            openValves.append(valve["key"])
            curPressure += valve["rate"]
            isOpening = False
    #elif not isMoving and isOpening:
    #    isOpening = False
        
    totalPressure += curPressure
    print("")