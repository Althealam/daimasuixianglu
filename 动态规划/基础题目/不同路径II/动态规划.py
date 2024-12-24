# 动态规划五部曲
# 1. dp含义：dp[i][j]表示到达[i][j]有多少种路径
# 2. 递推公式：dp[i][j]=dp[i-1][j]+dp[i][j-1]
# 3. 初始化：（本题和初始路径那道题的初始化是不一致的）如果遇到了障碍物，那么初始化就不变，仍然是0
# 原本的：dp[i][0]=1, dp[0][j]=1
# 如果第1行在第j列遇到了障碍物，那么在第j列后面的几列都为0
# 如果第1列在第i行遇到了障碍我，那么在第i行后面的几行都为0
# 4. 遍历顺序：从上往下，从左往右

# 时间复杂度：
# 1. 初始化dp数组：O(mn)
# 2. 初始化第一列：O(m)
# 3. 初始化第一行：O(n)
# 4. 计算dp数组的其余元素：O(mn)
# 总的时间复杂度：O(mn)
# 空间复杂度：
# 1. dp数组：O(mn)
# 总的空间复杂度：O(mn)

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid) # 行数
        n=len(obstacleGrid[0]) # 列数

        # 判断特殊情况
        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
            return 0

        # 构建dp二维数组
        dp=[[0]*n for _ in range(m)] # 只能初始化为0

        # 初始化dp
        # 1. 初始化第一列
        for i in range(m): 
            if obstacleGrid[i][0]==0: # 没有遇到障碍物
                dp[i][0]=1
            else: # 遇到了障碍物，则跳出循环，因为代表着i行后面的几行都是0
                break
        # 2. 初始化第一行
        for j in range(n):
            if obstacleGrid[0][j]==0: # 没有遇到障碍物
                dp[0][j]=1
            else: # 遇到了障碍物，则跳出循环，因为代表着j列后面的几列都是0
                break
        # 3. 初始化其他的行与列
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1: # 遇到了障碍物，那么仍然为0
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m-1][n-1]

            


        