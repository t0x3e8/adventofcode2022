import re

fContent = open("input.txt").readlines()
#stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]
stacks = [
    ["N", "S", "D", "C", "V", "Q", "T"],
    ["M", "F", "V"],
    ["F", "Q", "W", "D", "P", "N", "H", "M"],
    ["D", "Q", "R", "T", "F"],
    ["R", "F", "M", "N", "Q", "H", "V", "B"],
    ["C", "F", "G", "N", "P", "W", "Q"],
    ["W", "F", "R", "L", "C", "T"],
    ["T", "Z", "N", "S"],
    ["M", "S", "D", "J", "R", "Q", "H", "N"],
]


def move(n, s, e):
    index = len(stacks[e-1])
    for i in range(n):
        stacks[e - 1].insert(index, stacks[s - 1].pop())


for line in fContent:
    if line.startswith("move"):
        n, s, e = map(int, re.findall(r"[0-9]+", line))
        move(n, s, e)

r = ""
for i in range(len(stacks)):
    r += stacks[i][-1]
print(r)
