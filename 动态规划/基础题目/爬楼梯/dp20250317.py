# 1. dp数组以及下标的含义：dp[i]表示爬到第i层有dp[i]种方法
# 2. 递推公式：dp[i]=dp[i-1]+dp[i-2]
# 3. 初始化：dp[0]=1 dp[1]=1 dp[2]=2
# 4. 遍历顺序：从左到右
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        if n==0:
            return 1
        dp[1]=1
        if n==1:
            return 1
        dp[2]=2
        for i in range(3, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        