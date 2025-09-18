import collections
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[False]*m for _ in range(n)]
def bfs(i, j):
    queue = collections.deque()
    queue.append([i, j])
    while queue:
        cur_x, cur_y = queue.popleft()
        grid[cur_x][cur_y] = 2
        for dx, dy in directions:
            next_x, next_y = cur_x+dx, cur_y+dy
            if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                grid[next_x][next_y] =2
                visited[next_x][next_y]=True
                queue.append([next_x, next_y])

for i in range(n):
    if not visited[i][0] and grid[i][0]==1:
        bfs(i, 0)
    if not visited[i][m-1] and grid[i][m-1]==1:
        bfs(i, m-1)

for j in range(m):
    if not visited[0][j] and grid[0][j]==1:
        bfs(0, j)
    if not visited[n-1][j] and grid[n-1][j]==1:
        bfs(n-1, j)

for i in range(n):
    for j in range(m):
        if grid[i][j]==1:
            grid[i][j]=0

for i in range(n):
    for j in range(m):
        if grid[i][j]==2:
            grid[i][j]=1

for row in grid:
    print(' '.join(map(str, row)))