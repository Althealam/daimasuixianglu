# 1. dp数组以及下标的含义：dp[i][j]表示到达[i,j]的时候有dp[i][j]种方法
# 2. 递推公式：dp[i][j]=dp[i-1][j]+dp[i][j-1]
# 因为dp[i][j]只能从上面或者左边过来
# 3. dp数组的初始化：dp[i][0]=1 dp[0][j]=1
# 因为从(0,0)到(i,0)只有一条路径，并且(0,j)也同理
# 4. 遍历顺序：从左到右，从上到下

# 时间复杂度：O(mn)
# 空间复杂度：O(mn)

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[0]*n for _ in range(m)] # dp数组是m行n列的

        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        
        # 计算每个单元格的唯一路径数
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        
        return dp[m-1][n-1] # 返回右下角单元格的唯一路径数
        