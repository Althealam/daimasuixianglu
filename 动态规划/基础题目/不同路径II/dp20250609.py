# 1. dp数组以及下标的含义：dp[i][j]表示到达[i,j]有dp[i][j]条路径
# 2. 递推公式：dp[i][j]=dp[i-1][j]+dp[i][j-1]
# 3. 初始化：dp[i][0]=dp[i-1][0] dp[0][j]=dp[0][j-1] dp[0][0]=1 如果某个地方为障碍物，那么其后面的部分都为0
# 4. 遍历顺序：从上到下，从左到右

def ditui(grid):
    m, n = len(grid), len(grid[0])
    # 初始化
    dp=[[0]*n for _ in range(m)]
    # 判断特殊条件
    if grid[m-1][n-1]==1 or grid[0][0]==1:
        return 0
    dp[0][0]=1
    # 初始化第一列，如果遇到障碍物则直接退出
    for i in range(m):
        if grid[i][0]==0:
            dp[i][0]=1
        else:
            break
    # 初始化第一行，如果遇到障碍物则直接退出
    for j in range(n):
        if grid[0][j]==0:
            dp[0][j]=1
        else:
            break
    
    # 开始递推
    for i in range(1,m):
        for j in range(1,n):
            if grid[i][j]==1: # 遇到障碍物
                continue
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    
    return dp[-1][-1]

grid=[[0,0,0], [0,1,0], [0,0,0]]
result=ditui(grid)
print(result)