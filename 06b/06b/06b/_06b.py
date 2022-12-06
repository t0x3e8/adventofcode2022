fContent = open("input.txt", "r").read()

def isCharDup(seq):
    for j in range(len(seq)-1):
        for k in range(j+1, len(seq)): 
            if seq[j] == seq[k]: return True

pos = 0 
for i in range(len(fContent)):
    seq = fContent[i:i+14]
    if not isCharDup(seq):
        pos = i + 14
        break

print("Start-of-packet marker:", pos)
        