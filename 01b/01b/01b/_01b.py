import numpy as np

fContent =  open("input.txt", "r").readlines();
caloriesSum = 0;
totals = []

for line in fContent:
    if line == "\n":
        totals.append(caloriesSum)
        caloriesSum = 0
    else:
        caloriesSum += int(line);


top3 = np.sort(totals)[-3: ]

print(np.sum(top3))