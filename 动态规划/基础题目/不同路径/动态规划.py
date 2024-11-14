# 动态规划五部曲
# 1. dp数组的含义：dp[i][j]代表的是从[0,0]到[i,j]有多少种不同的路径
# 2. 递推公式：由于机器人每次只能向下或者向右走。因此，到达(i,j)只可能是从(i+1,j)或者(i,j-1)过来的
# dp[i][j]=dp[i-1][j]+dp[i][j-1]
# 3. 初始化：一定需要初始化i=0与j=0的部分
# dp[0][j]=1 dp[i][0]=1（由于机器人只能向下或者向右走，因此这两种都只有一种走法）
# 4. 遍历顺序：从左往右走，从上往下走
# 5. 打印dp数组

# 时间复杂度：
# 1. 初始化dp数组：O(mxn)
# 2. 填充第一列和第一行：O(m+n)
# 3. 计算每个单元格的唯一路径数：O(mxn)
# 总的时间复杂度：O(mxn)
# 空间复杂度：
# 1. dp数组：O(mxn)
# 总的空间复杂度：O(mxn)

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[[0]*n for _ in range(m)] # 定义n*m维矩阵

        # 设置第一行和第一列的基本情况
        for i in range(m): # 第一列
            dp[i][0]=1
        for j in range(n): # 第一行
            dp[0][j]=1
        
        # 计算每个单元格的唯一路径数
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
            
        # 返回右下角单元格的唯一路径数
        return dp[m-1][n-1]
        