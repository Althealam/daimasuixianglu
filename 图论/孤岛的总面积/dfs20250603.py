n, m = map(int, input().split())

grid=[]
for _ in range(n):
    grid.append(list(map(int, input().split())))

count=0 

def dfs(grid, i, j):
    global count
    position=[[1, 0], [-1, 0], [0, 1], [0, -1]]
    grid[i][j]=0
    count+=1
    for x, y in position:
        next_x=x+i
        next_y=y+j
        if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
            continue
        if grid[next_x][next_y]==1:
            dfs(grid, next_x, next_y)

# 清除边界的连通分量
# 1. 清除左右两个边界
for i in range(n):
    if grid[i][0]==1:
        dfs(grid, i, 0)
    if grid[i][m-1]==1:
        dfs(grid, i, m-1)

# 2. 清除上下两个边界
for j in range(m):
    if grid[0][j]==1:
        dfs(grid, 0, j)
    if grid[n-1][j]==1:
        dfs(grid, n-1, j)

count=0
for i in range(n):
    for j in range(m):
        if grid[i][j]==1:
            dfs(grid, i, j)
print(count)