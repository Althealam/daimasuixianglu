def dfs(visited, grid, x, y):
    direction=[[1,0], [-1,0], [0,1], [0, -1]]
    count=1 # 当前单元格的岛屿面积

    if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
        return 0
    if visited[x][y] or grid[x][y]!=1:
        return 0
    visited[x][y]=True
    for i,j in direction:
        next_x=x+i
        next_y=y+j
        count+=dfs(visited, grid, next_x, next_y)
    return count


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
            count=dfs(visited, grid, i, j)
            res=max(res, count)
print(res)