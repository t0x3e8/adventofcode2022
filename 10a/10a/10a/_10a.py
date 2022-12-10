fContent = open("input.txt", "r").readlines()

def p(ccl, X, line):
    if ccl == 20 or ccl >= 60 and (ccl-20) %40 == 0  :
        print(f"Cycle: {ccl}, X: {X}, line: {line}")
        return ccl*X
    
    return 0


def Part1():
    ccl = 0
    X = 1
    total = 0

    for line in fContent:
        ccl += 1
        total = total + p(ccl, X, line)
        inst = line[:4]
        
        if inst == "addx":
            V = int(line.strip()[5:])
            ccl += 1   
            total = total + p(ccl, X, line)
            X += V
    return total

total = Part1()
print(f"total: {total}")