fContent = open("input.txt", "r").read()
numbers = list(enumerate(map(int, fContent.split("\n"))))
numbersCopy = numbers.copy()
l = len(numbers)
zeroIndex = 0

for n in numbers:
    oldIndex = numbersCopy.index(n)
    newIndex = (n[1] + oldIndex) % (l - 1)    
    numbersCopy.insert(newIndex, numbersCopy.pop(oldIndex))

for i in range(0, l): 
    if numbersCopy[i][1] == 0:
        zeroIndex = i
        break
    
l1 = numbersCopy[(zeroIndex + 1000) % len(numbersCopy)][1]
l2 = numbersCopy[(zeroIndex + 2000) % len(numbersCopy)][1]
l3 = numbersCopy[(zeroIndex + 3000) % len(numbersCopy)][1]
print(f"{l1} + {l2} + {l3} = {l1 + l2 + l3}")    