# 1. dp数组以及下标的含义：dp[i][j]表示从(0,0)出发到(i,j)有dp[i][j]条路径
# 2. 确定递推公式：dp[i][j]=dp[i-1][j]+dp[i][j-1]
# 3. dp数组的初始化：
# 在没有障碍物的情况下：dp[i][0]=1 dp[0][j]=1
# 有障碍物的情况下：如果障碍物是在第一行或者第一列上，那么障碍物后面的几列都是0，障碍物后面的几行都是0
# 4. 递推顺序：从左到右，从上到下

# 时间复杂度：O(m*n)
# 空间复杂度：O(m*n)

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid) # 求数组的行数
        n=len(obstacleGrid[0]) # 求数组的列数
        # 如果终点位置或者起始位置本身就有障碍物，则永远无法到达
        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
            return 0
        dp=[[0]*n for _ in range(m)]

        # 初始化第一列的dp数组
        for i in range(m):
            if obstacleGrid[i][0]==0:
                dp[i][0]=1
            # 遇到了障碍物，则默认后面的都是0
            else:
                break
        
        # 初始化第一行的dp数组
        for j in range(n):
            if obstacleGrid[0][j]==0:
                dp[0][j]=1
            else:
                break
        
        # 递归求解数组
        # 第一行和第一列都已经初始化过了，因此不需要从0开始，从1开始即可
        for i in range(1,m):
            for j in range(1,n):
                # 如果遇到了障碍物，则直接跳过
                if obstacleGrid[i][j]==1:
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        
        return dp[m-1][n-1]

        