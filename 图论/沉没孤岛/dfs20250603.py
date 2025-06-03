n, m = map(int, input().split())
grid=[]
for _ in range(n):
    grid.append(list(map(int, input().split())))

def dfs(grid, x, y):
    grid[x][y]=2
    directions=[[1,0], [-1, 0], [0, 1], [0, -1]]
    for dx, dy in directions:
        next_x=x+dx
        next_y=y+dy
        if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
            continue
        if grid[next_x][next_y]==0 or grid[next_x][next_y]==2:
            continue
        dfs(grid, next_x, next_y)
    
for i in range(n):
    if grid[i][0]==1:
        dfs(grid, i, 0)
    if grid[i][m-1]==1:
        dfs(grid, i, m-1)

for j in range(m):
    if grid[0][j]==1:
        dfs(grid, 0, j)
    if grid[n-1][j]==1:
        dfs(grid, n-1, j)

for i in range(n):
    for j in range(m):
        if grid[i][j]==1:
            grid[i][j]=0
        if grid[i][j]==2:
            grid[i][j]=1

for row in grid:
    print(' '.join(map(str, row)))