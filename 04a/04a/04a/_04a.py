fContent =  open("Input.txt", "r").readlines();

def toWord(sec):
    word = ""
    r = sec.split("-")
    for i in range(int(r[0]), int(r[1])+1):
        word += (str(i))
    return word

redundantPairs = 0
for line in fContent:
    sections = line.split(",")
    s1 = toWord(sections[0])
    s2 = toWord(sections[1])

    if s1 in s2 or s2 in s1:
        redundantPairs += 1

print("Redundant pairs: ", redundantPairs)
    
