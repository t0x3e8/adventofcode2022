fContent =  open("input.txt", "r").readlines();

redundantPairs = 0

lineNumber = []
for line in fContent:
    sections = line.split(",")
    r1 = sections[0].split("-")
    r2 = sections[1].split("-")
    s1, e1 = int(r1[0]), int(r1[1])
    s2, e2 = int(r2[0]), int(r2[1])

    if (s2 >= s1 and s2 <= e1) or (s1 >= s2 and s1 <= e2):
        redundantPairs += 1
        print(line)

print("Redundant pairs: ", redundantPairs)