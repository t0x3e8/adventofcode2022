fContent = open("input.txt", "r").readlines();
dirs = [];
cur = "/"

def cd(cmd):
    global cur
    if cmd.startswith("..") : cur = cur[0: cur.rindex("/")]
    elif cmd == "/" : cur = "/"
    else: cur += cmd + "/"

def ls(size):
    dirs.append((cur, size))
        
i = 0
while True:
    if i == (len(fContent)-1): break
    line = fContent[i]
    if line.startswith("$ cd"): 
        cd(line[5:].strip())
        i += 1
    elif line.startswith("$ ls"):
        sizeTotal = 0
        for j in range(i+1, len(fContent)):
            line = fContent[j]
            if line.startswith("$"): break
            elif not line.startswith("dir"):
                size = int(line.split(" ")[0])
                sizeTotal += size
        
        ls(sizeTotal)
        i = j
    else: 
        i += 1

total = 0
for i in range(len(dirs)):
    d = dirs[i]
    sizes = [dirs[i][1] for i, _d in enumerate(dirs) if _d[0].startswith(d[0])]
    dirs[i] = (dirs[i][0], dirs[i][1], sum(sizes))
    
    if dirs[i][2] <= 100000:
        total += dirs[i][2]

print(total)