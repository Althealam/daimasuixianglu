direction=[[1,0],[-1,0],[0,1],[0,-1]]
result=0

# DFS
def dfs(grid,y,x):
    grid[y][x]=0
    global result
    result+=1

    for i,j in direction:
        next_x=x+j
        next_y=y+i
        if (next_x<0 or next_y<0 or next_x>=len(grid[0]) or next_y>=len(grid)):
            continue
        if grid[next_y][next_x]==1 and not visited[next_y][next_x]:
            visited[next_y][next_x]=True
            dfs(grid,next_y,next_x)

# 读取输入值
n,m=map(int,input().split())
grid=[]
visited=[[False]*m for _ in range(n)]

for i in range(n):
    grid.append(list(map(int,input().split())))

# 处理边界
for j in range(m):
    # 上边界
    if grid[0][j]==1 and not visited[0][j]:
        visited[0][j]=True
        dfs(grid,0,j)
    # 下边界
    if grid[n-1][j]==1 and not visited[n-1][j]:
        visited[n-1][j]=True
        dfs(grid,n-1,j)   


for i in range(n):
    # 左边界
    if grid[i][0]==1 and not visited[i][0]:
        visited[i][0]=True
        dfs(grid,i,0)
    # 右边界
    if grid[i][m-1]==1 and not visited[i][m-1]:
        visited[i][m-1]=True
        dfs(grid,i,m-1)

# 计算孤岛总面积
result=0

for i in range(n):
    for j in range(m):
        if grid[i][j]==1 and not visited[i][j]:
            visited[i][j]=True
            dfs(grid,i,j)

# 输出孤岛的总面积
print(result)
