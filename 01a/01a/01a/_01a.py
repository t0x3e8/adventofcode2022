fContent =  open("input.txt", "r").readlines();
caloriesSum = 0;
totals = []

for line in fContent:
    if line == "\n":
        totals.append(caloriesSum)
        caloriesSum = 0
    else:
        caloriesSum += int(line);

print(max(totals))