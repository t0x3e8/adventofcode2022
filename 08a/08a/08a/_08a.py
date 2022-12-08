fContent = open("input.txt", "r").readlines()

wSize, hSize = len(fContent[0].strip()), len(fContent);
edgeCount =  (2 * hSize) + (2 * wSize) - 4

def countTrees(trees, w, h, isVertical):
    for x in range(1, w):
        tHighest  = int(fContent[0][x]) if isVertical else int(fContent[x][0])
        _tHighest = int(fContent[h][x]) if isVertical else int(fContent[x][h])
        for y in range(1, h):
            _y = h - y 
            t  = int(fContent[y][x])  if isVertical else int(fContent[x][y])
            _t = int(fContent[_y][x]) if isVertical else int(fContent[x][_y])

            if  t > tHighest:
                trees.append(f"{x}-{y}({t})" if isVertical else f"{y}-{x}({t})")
                tHighest = t                
            if _t > _tHighest :
                trees.append(f"{x}-{_y}({_t})" if isVertical else f"{_y}-{x}({_t})")
                _tHighest = _t

trees = []
countTrees(trees, wSize - 1, hSize - 1, True)
countTrees(trees, hSize - 1, wSize - 1, False)

i = 0
for t in list(dict.fromkeys(trees)):
    print(t)
    i += 1

print(f"Total trees: {i}+{edgeCount}=", i + edgeCount)
