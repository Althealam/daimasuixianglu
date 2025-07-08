# 1. dp数组以及下标的含义：dp[i][j]表示从三角形顶部走到[i,j]的最小路径和，其中[i,j]表示的是第i行第j列的位置
# 2. 递推公式：dp[i][j]=min(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]
# 由于每一步只能移动到下一行相邻的节点上，因此想要走到位置[i,j]，上一步只能在位置[i-1, j-1]或者位置[i-1,j]
# 3. 遍历顺序：
# 4. 初始化：dp[i][0]=dp[i-1][0]+triangle[i][0] 

# 时间复杂度：O(n**2)
# 空间复杂度：O(n**2)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0]* n for _ in range(n)]
        dp[0][0]=triangle[0][0]

        for i in range(1, n):
            dp[i][0] = dp[i-1][0]+triangle[i][0] # 初始化dp[i][0]
            for j in range(1, i):
                dp[i][j]=min(dp[i-1][j-1], dp[i-1][j])+triangle[i][j]
            dp[i][i]=dp[i-1][i-1]+triangle[i][i]

        return min(dp[n-1]) # 最后一行的最小值