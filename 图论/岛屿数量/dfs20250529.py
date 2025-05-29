# n行m列
direction=[[0, 1], [1, 0], [0, -1], [-1, 0]]
def dfs(visited, grid, x, y):
    """
    深搜该岛屿的其他节点
    :param visited: 访问表
    :param grid: 邻接矩阵
    :param x: 当前遍历的节点的x值
    :param y: 当前遍历的节点的y值
    """
    for i, j  in direction:
        next_x=x+i
        next_y=y+j
        if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
            continue
        if not visited[next_x][next_y] and grid[next_x][next_y]==1:
            visited[next_x][next_y]=True
            dfs(visited, grid, next_x, next_y)



# 读取岛屿矩阵的行和列数
n, m=map(int, input().split())

# 构建岛屿矩阵
grid=[] # 注意不要初始化
for i in range(n):
    grid.append(list(map(int, input().split())))

# 访问表
visited=[[False]*m for _ in range(n)]

# 岛屿数量
res=0

# 统计岛屿数量
for i in range(n):
    for j in range(m):
        if grid[i][j]==1 and not visited[i][j]:
            res+=1
            # 标记为已访问过
            visited[i][j]=True
            dfs(visited, grid, i, j)
print(res)