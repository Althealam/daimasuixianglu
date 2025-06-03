from collections import deque
def bfs(visited, grid, x, y):
    if grid[x][y]!=1 or visited[x][y]:
        return 0
    que=deque([(x, y)])
    visited[x][y]=True
    area=0 # 当前遍历的岛屿的面积

    directions=[[0, 1], [0, -1], [1, 0], [-1, 0]]
    while que:
        i, j =que.popleft()
        area+=1
        for di, dj in directions:
            next_x, next_y=i+di, j+dj
            if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                visited[next_x][next_y]=True
                que.append((next_x, next_y))
    return area


n, m = map(int, input().split())
# n行m列

# 构建岛屿矩阵
grid=[]
for i in range(n):
    grid.append(list(map(int, input().split())))

# 访问表
visited=[[False]*m for _ in range(n)]

# 岛屿的最大面积
res=0


for i in range(n):
    for j in range(m):
        if grid[i][j]==1 and not visited[i][j]:
            count=bfs(visited, grid, i, j)
            res=max(res, count)
print(res)