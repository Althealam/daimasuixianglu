# 1. dp数组以及下标的含义：dp[i][j]表示从[0,0]走到[i,j]的最小路径和为dp[i][j]
# 2. 递推公式：
# dp[i][j]=min(dp[i-1][j], dp[i][j-1])+grid[i][j]
# 3. 初始化：全部初始化为0 dp[0][0]=grid[0][0] dp[0][j]=dp[0][j-1]+grid[0][j] dp[i][0]=dp[i-1][0]+grid[i][0]
# 4. 遍历顺序：从前向后
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp=[[0]*len(grid[0]) for _ in range(len(grid))]
        dp[0][0]=grid[0][0]
        for i in range(1, len(grid)):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(1, len(grid[0])):
            dp[0][j]=dp[0][j-1]+grid[0][j]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j]=min(dp[i-1][j], dp[i][j-1])+grid[i][j]
        return dp[-1][-1]        