fContent =  open("Input.txt", "r").readlines();

redundantPairs = 0

lineNumber = []
for line in fContent:
    sections = line.split(",")
    r1 = sections[0].split("-")
    r2 = sections[1].split("-")
    s1, e1 = int(r1[0]), int(r1[1])+1
    s2, e2 = int(r2[0]), int(r2[1])+1

    if (s1 <= s2 and e1 >= e2) or (s1 >= s2 and e1 <= e2):
        redundantPairs += 1

print("Redundant pairs: ", redundantPairs)