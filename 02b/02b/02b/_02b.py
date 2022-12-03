import numpy as np

fContent =  open("input.txt", "r").readlines();

def changeSeq(seq):
     if seq in xArr: return "X";
     elif seq in yArr: return "Y";
     else: return "Z";


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
xArr = np.array(["C Z", "A Y", "B X"])
yArr = np.array(["C X", "A Z", "B Y"])
sum = 0

for line in fContent:
    line = line[:2] + changeSeq(line.strip()) + line[3:]
    print(line)
    battlePoints = getBattlePoints(line.strip())
    shapePoints = getShapePoints(line[2])
    sum += battlePoints + shapePoints


print(sum)
