# 1. dp数组以及下标的含义：dp[i]表示下标为i的斐波那契数
# 2. 递推公式：dp[i]=dp[i-1]+dp[i-2]
# 3. 初始化：dp[0]=0 dp[1]=1
# 4. 遍历顺序：从左到右
class Solution:
    def fib(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=0
        if n==0:
            return 0
        dp[1]=1
        if n==1:
            return 1
        for i in range(2, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        