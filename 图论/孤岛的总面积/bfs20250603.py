from collections import deque
n, m = map(int, input().split())

grid=[]
for _ in range(n):
    grid.append(list(map(int, input().split())))

count=0 

def bfs(grid, i, j):
    global count
    q=deque()
    q.append((i, j))
    count+=1
    grid[i][j]=0
    directions=[[0, 1], [0, -1], [1, 0], [-1, 0]]

    while q:
        x, y = q.popleft()
        for di, dj in directions:
            ni, nj=x+di, y+dj
            if ni<0 or nj<0 or ni>=len(grid) or nj>=len(grid[0]):
                continue
            if grid[ni][nj]==1:
                q.append((ni, nj))
                grid[ni][nj]=0
                count+=1

# 清除边界的连通分量
# 1. 清除左右两个边界
for i in range(n):
    if grid[i][0]==1:
        bfs(grid, i, 0)
    if grid[i][m-1]==1:
        bfs(grid, i, m-1)

# 2. 清除上下两个边界
for j in range(m):
    if grid[0][j]==1:
        bfs(grid, 0, j)
    if grid[n-1][j]==1:
        bfs(grid, n-1, j)

count=0
for i in range(n):
    for j in range(m):
        if grid[i][j]==1:
            bfs(grid, i, j)
print(count)