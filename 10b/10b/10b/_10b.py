
fContent = open("testinput.txt", "r").readlines()

def p(ccl, X, line):
    if ccl % 40 == 0:
        print("Cycle -> ")
    elif ccl % 39 == 0:
        print(" <- Cycle")
    #if ccl == 20 or ccl >= 60 and (ccl-20) %40 == 0  :
        #print(f"Cycle: {ccl}, X: {X}, line: {line}")


def Part2():
    ccl = 0
    X = 1

    for line in fContent:
        ccl += 1
        p(ccl, X, line)
        inst = line[:4]
        
        if inst == "addx":
            V = int(line.strip()[5:])
            ccl += 1   
            p(ccl, X, line)
            X += V

Part2()