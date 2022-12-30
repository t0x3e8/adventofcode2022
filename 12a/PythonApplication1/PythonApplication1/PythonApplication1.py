def readData(path):
    data = []
    with open(path, "r") as fContent:
        for line in fContent.readlines():
            data.append(list(line.strip()))

    return data

def DFS(grid, startRow, startCol): 
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    steps = [[1 for _ in range(cols)] for _ in range(rows)]
    queue = [(startRow, startCol)]
    
    while queue:
        row, col = queue.pop(0)
        if not visited[row][col]:
            visited[row][col] = True
            
            for r, c in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
                if 0 <= r < rows and 0 <= c < cols and not visited[r][c]:
                    if grid[r][c] == "E" and grid[row][col] == "z":
                        print(f"Shortest path consists of {steps[row][col]} steps.")
                        return (visited, steps)
                    if grid[r][c] == grid[row][col] or grid[r][c] == chr(ord(grid[row][col]) + 1): 
                        queue.append((r, c))
                        steps[r][c] = steps[row][col] + 1

    return (visited, steps)

data = readData("input.txt")
SPos = [(iy, ix) for iy, row in enumerate(data) for ix, c in enumerate(row) if c == "S"][0]
data[SPos[0]][SPos[1]] = "a"

visted, steps = DFS(data, SPos[0], SPos[1])



# PRINTING ---------------------------------------
print("visited-------------------------")
for row in visted:
    for cell in row:
        print(f"[{int(cell)}] ", end="")
    print("\n")
    
print("steps----------------------------")
for row in steps:
    for cell in row:
        print(f"[{int(cell)}] ", end="")
    print("\n")

print("values---------------------------")
for row in data:
    for cell in row:
        print(f"[{cell}] ", end="")
    print("\n")
