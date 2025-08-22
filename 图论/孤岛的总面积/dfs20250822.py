n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[False]*m for _ in range(n)]
ans = 0
def dfs(i, j):
    visited[i][j]=True
    grid[i][j] = 0
    for dx, dy in directions:
        next_x, next_y = i+dx, j+dy
        if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
            continue
        if not visited[next_x][next_y] and grid[next_x][next_y]==1:
            grid[next_x][next_y] = 0
            visited[next_x][next_y] = True
            dfs(next_x, next_y)


for i in range(n):
    if not visited[i][0] and grid[i][0]==1:
        dfs(i, 0)
    if not visited[i][m-1] and grid[i][m-1]==1:
        dfs(i, m-1)

for j in range(m):
    if not visited[0][j] and grid[0][j]==1:
        dfs(0, j)
    if not visited[n-1][j] and grid[n-1][j]==1:
        dfs(n-1, j)

for i in range(n):
    for j in range(m):
        if grid[i][j]!=0:
            ans+=1
print(ans)
