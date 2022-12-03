import numpy as np

fContent =  open("input.txt", "r").readlines();

def getBattlePoints(seq):
     if seq in sixArr: return 6;
     elif seq in threeArr: return 3;
     else: return 0;

def getShapePoints(seq):
     if seq == "X": return 1;
     elif seq == "Y": return 2;
     else: return 3;

sixArr = np.array(["C X", "B Z", "A Y"])
threeArr = np.array(["C Z", "A X", "B Y"])
zeroArr = np.array(["C Y", "A Z", "B X"])
sum = 0

for line in fContent:
    battlePoints = getBattlePoints(line.strip())
    shapePoints = getShapePoints(line[2])
    sum += battlePoints + shapePoints


print(sum)


#C	Z	3
#C	X	6
#C	Y	0
#A	Z	0
#B	Z	6
#A	X	3
#A	Y	6
#B	X	0
#B	Y	3