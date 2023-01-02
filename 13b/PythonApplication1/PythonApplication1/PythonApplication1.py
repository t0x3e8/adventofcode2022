
def readPairs(fileName):
    pairs = []
    with open(fileName, "r") as fContent:
        for line in fContent.readlines():
            if line.strip():
                pairs.append(eval(line.strip()))

    return pairs

def compare(l, r):
    for i in range(max(len(l), len(r))):
        if i >= len(l):
            #print("Left side ran out of items, so inputs are in the right order")
            return True
        elif i >= len(r): 
            #print("Right side ran out of items, so inputs are NOT in the right order")
            return False
        
        if isinstance(l[i], int) and isinstance(r[i], int):
            #print(f"Compare {l[i]} vs {r[i]}")
            if l[i] == r[i]: continue
            elif l[i] < r[i]: 
                #print("Left side is smaller, so inputs are in the right order")
                return True
            else:
                #print("Right side is smaller, so inputs are NOT in the right order")
                return False
        else:
            
            ll = [l[i]] if isinstance(l[i], int) else l[i]
            rr = [r[i]] if isinstance(r[i], int) else r[i]
            result = compare(ll, rr)
            if result != None: return result

    return None

def sort(packets):
    swap = True

    while swap:
        swap = False
        for i in range(len(packets) - 1):
            if compare(packets[i+1], packets[i]):
                packets[i], packets[i+1] = packets[i+1], packets[i]
                swap = 1

    return packets

packets = readPairs("input.txt")
packets.append([[2]])
packets.append([[6]])

sortedList = sort(packets)

for p in sortedList:
    print(p)

ix2 = [i for i, p in enumerate(sortedList) if(p == [[2]])][0] + 1
ix9 = [i for i, p in enumerate(sortedList) if(p == [[6]])][0] + 1

print("The decoder key for the distress signal is: ", ix2 * ix9)