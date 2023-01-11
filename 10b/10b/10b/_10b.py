fContent = open("input.txt", "r").readlines()

def print2(px):
    i = 0
    for row in px:
        print("Cycle ","{:3d}".format(i + 1)," -> ", end="")
        for c in row:
            print(c, end="")
        print(" <- Cycle", "{:3d}".format(i + 40))
        i += 40
        
def Part2(px):
    ccl = 0
    x = 1

    for line in fContent:
        for _ in range(2):
            ccl += 1
            crow, cpix = divmod(ccl-1, 40)
            if x-1 <= cpix <= x+1: 
                px[crow][cpix] = '#'
            else: 
                px[crow][cpix] = '.'
            
            if not line.startswith('add'): break

        else: 
            x += int(line.strip()[5:])

    
px = [['.']*40 for _ in range(6)]
Part2(px)
print2(px)