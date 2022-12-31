from collections import deque
import time

def readData(path):
    data = []
    with open(path, "r") as fContent:
        for line in fContent.readlines():
            data.append([ord(c) for c in line.strip()])

    return data

def getNeighbors(grid, row, col, rows, cols):
    result = []
    for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
        if 0 <= r < rows and 0 <= c < cols:
            if grid[row][col] <= grid[r][c] <= (grid[row][col] + 1):
                result.append((r, c))
    return result
     
def countMoves(visited):
    lvisited = list(visited.items())
    node = lvisited[-1]
    counter = 0
    while True:
        nodes = [element for element in lvisited if element[0] == node[1]]
        if len(nodes) == 0: break
        else:
            counter += 1
            node = nodes[0]
    return counter

def BFS(grid, startPos, endPos): 
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    movements = { (startPos[0], startPos[1]) : None }
    queue = deque([(startPos[0], startPos[1])], 20000000)
    
    while queue:
        row, col = queue.popleft()
        if row == endPos[0] and col == endPos[1]:
            return movements
        
        visited.add((row, col))

        for r, c in getNeighbors(grid, row, col, rows, cols):
            if (r, c) not in visited:
                queue.append((r, c))
                movements[(r, c)] = (row, col)
                
data = readData("input.txt")
SPos = [(iy, ix) for iy, row in enumerate(data) for ix, c in enumerate(row) if c == ord("S")][0]
EPos = [(iy, ix) for iy, row in enumerate(data) for ix, c in enumerate(row) if c == ord("E")][0]
data[SPos[0]][SPos[1]] = ord("a")
data[EPos[0]][EPos[1]] = ord("z")

startTimer = time.time()
visited = BFS(data, SPos, EPos)
endTimer = time.time()
elapsedTimer = endTimer - startTimer

print(f"Time elapsed: {elapsedTimer:.5f} seconds")
print(f"Steps count: {countMoves(visited)}")