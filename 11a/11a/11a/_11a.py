import re, math, numpy as np

fContent = open("input.txt", "r").read()
monkeys = []

mSet = [re.findall(r"Starting items: (.*)", fContent),
           re.findall(r"Operation: new = (.*)", fContent), 
           re.findall(r"Test: divisible by (.*)", fContent),
           re.findall(r"If true: throw to monkey (.*)", fContent),
           re.findall(r"If false: throw to monkey (.*)", fContent)]

for i in range(len(mSet[0])):
    monkeys.append([re.findall(r"\d+", mSet[0][i]),
            mSet[1][i],
            re.findall(r"\d+", mSet[2][i]),
            re.findall(r"\d+", mSet[3][i]),
            re.findall(r"\d+", mSet[4][i]),
            0])
    
for r in range(20):
    for mIndex in range(len(monkeys)):
        while len(monkeys[mIndex][0]) > 0:
            item = monkeys[mIndex][0].pop()
            monkeys[mIndex][5] += 1
            wl = eval(monkeys[mIndex][1].replace("old", str(item)))
            wl = math.floor(wl / 3)
            test = wl % int(monkeys[mIndex][2][0]) == 0
            if test:
                monkeys[int(monkeys[mIndex][3][0])][0].append(wl)
            else:
                monkeys[int(monkeys[mIndex][4][0])][0].append(wl)
                
inspectedItems = []
for mIndex in range(len(monkeys)):
    inspectedItems.append(monkeys[mIndex][5])

inspectedItems.sort(reverse=True)
print(inspectedItems[0] * inspectedItems[1])


