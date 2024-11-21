# DFS
# 分析：这道题和101.孤岛的总面积相反，本题是将孤岛变成0，而101.孤岛的总面积是将非孤岛变成0
# 思路：从地图周边出发，将周边空格相邻的陆地都做上标记，然后再遍历一遍地图，遇到陆地并且没做过标记的，那么就是地图中间的陆地，改成水域即可
# 1. DFS或者BFS将地图周边的1（陆地）改成2（特殊标记）
# 2. 将水域中间1（陆地）全部改成水域（0）
# 3. 将之前标记的2改为1（陆地）

def dfs(grid,x,y):
    grid[x][y]=2
    directions=[(-1,0),(1,0),(0,1),(0,-1)]
    for dx, dy in directions:
        nextx,nexty=x+dx,y+dy
        # 超过边界
        if nextx<0 or nextx>=len(grid) or nexty<0 or nexty>=len(grid[0]):
            continue
        # 不符合条件，不继续遍历
        if grid[nextx][nexty]==0 or grid[nextx][nexty]==2:
            continue
        dfs(grid,nextx,nexty)

def main():
    n,m=map(int,input().split())
    grid=[[int(x) for x in input().split()] for _ in range(n)]
    
    # 步骤一
    # 从左侧边和右侧边，向中间遍历
    for i in range(n):
        if grid[i][0]==1: # 左边界
            dfs(grid,i,0)
        if grid[i][m-1]==1: # 右边界
            dfs(grid,i,m-1)
            
    # 从上边和下边，向中间遍历
    for j in range(m):
        if grid[0][j]==1:
            dfs(grid,0,j)
        if grid[n-1][j]==1:
            dfs(grid,n-1,j)
    
    # 步骤二、步骤三：修改grid[i][j]==2的为1，修改grid[i][j]==1的为0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                grid[i][j]=0
            if grid[i][j]==2:
                grid[i][j]=1
    
    # 打印结果
    for row in grid:
        print(' '.join(map(str,row)))

if __name__=='__main__':
    main()