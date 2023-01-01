def readPairs(fileName):
    pairs = []
    with open(fileName, "r") as fContent:
        for line in fContent.readlines():
            if line.strip():
                pairs.append(eval(line.strip()))

    return pairs

def isPairOrderRight(l, r):
    for i in range(max(len(l), len(r))):
        if i >= len(l):
            print("Left side ran out of items, so inputs are in the right order")
            return True
        elif i >= len(r): 
            print("Right side ran out of items, so inputs are NOT in the right order")
            return False
        
        if isinstance(l[i], int) and isinstance(r[i], int):
            print(f"Compare {l[i]} vs {r[i]}")
            if l[i] == r[i]: continue
            elif l[i] < r[i]: 
                print("Left side is smaller, so inputs are in the right order")
                return True
            else:
                print("Right side is smaller, so inputs are NOT in the right order")
                return False
        else:
            
            ll = [l[i]] if isinstance(l[i], int) else l[i]
            rr = [r[i]] if isinstance(r[i], int) else r[i]
            result = isPairOrderRight(ll, rr)
            if result != None: return result

    return None

pairs = readPairs("input.txt")
results = []
for i in range(0, len(pairs), 2):
    l = pairs[i]
    r = pairs[i+1]
    result = isPairOrderRight(l, r)
    results.append((i / 2 + 1, result))

print("The sum of the indices of right pairs? ", sum(r[0] for r in results if r[1]))