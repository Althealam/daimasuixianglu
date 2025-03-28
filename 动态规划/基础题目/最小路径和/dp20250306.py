# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

# 说明：每次只能向下或者向右移动一步。

# 示例 1：

# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
# 示例 2：

# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12

# 1. dp数组以及下标的含义：dp[i][j]表示到达(i,j)位置的最小数字总和
# 2. 递推公式：dp[i][j]=min(dp[i-1][j], dp[i][j-1])+grid[i][j]
# 3. 遍历顺序：从左到右，从上到下
# 4. 初始化：dp[i][0]=grid[i][0] dp[0][j]=sum(grid[0][)

def pathsum(grid):
    m=len(grid)
    n=len(grid[0])
    dp=[[0]*n for _ in range(m)]
    dp[0][0]=grid[0][0]
    for j in range(1,n):
        dp[0][j]=dp[0][j-1]+grid[0][j]
    
    for i in range(1, m):
        dp[i][0]=dp[i-1][0]+grid[i][0]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j]=min(dp[i-1][j], dp[i][j-1])+grid[i][j]
    print(dp)
    return dp[-1][-1]

grid=[[1,3,1],[1,5,1],[4,2,1]]
print(pathsum(grid))
