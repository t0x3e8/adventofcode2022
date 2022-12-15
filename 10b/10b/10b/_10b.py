
fContent = open("testinput.txt", "r").readlines()

#def p(ccl, X, line):
#    if ccl % 40 == 0:
#        print("Cycle ","{:3d}".format(ccl)," -> ", end="")
#    elif ccl % 39 == 0:
#        print(" <- Cycle")
#    #if ccl == 20 or ccl >= 60 and (ccl-20) %40 == 0  :
#        #print(f"Cycle: {ccl}, X: {X}, line: {line}")

def p(px):
    for i in range(0, len(px), 40):
        print("Cycle ","{:3d}".format(i + 1)," -> ", end="")
        for j in range(0, 40):
            print(px[i+j], end="")
        print(" <- Cycle", "{:3d}".format(i + j + 1))

def Part2():
    ccl = 0
    X = 1
    px  = ["#"] * 240
    p(px)

    for line in fContent:
        ccl += 1
        #p(ccl, X, line)
        inst = line[:4]
        
        if inst == "addx":
            V = int(line.strip()[5:])
            ccl += 1   
            #p(ccl, X, line)
            X += V

    #p(ccl + 1, X, "")

Part2()