import collections
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

ans = 0 # 岛屿的数量
visited = [[False]*m for _ in range(n)] # 是否访问节点
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def bfs(i, j):
    queue = collections.deque()
    queue.append([i, j])
    while queue:
        cur_x, cur_y = queue.popleft()
        for dx, dy in directions:
            next_x, next_y = cur_x+dx, cur_y+dy
            if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                visited[next_x][next_y] = True
                queue.append([next_x, next_y])


for i in range(n):
    for j in range(m):
        if grid[i][j]==1 and not visited[i][j]:
            ans+=1
            bfs(i, j)
print(ans)