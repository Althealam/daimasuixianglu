# 1. dp数组以及下标的含义：dp[i]表示分拆数字i，可以得到的最大乘积
# 2. 递推公式：dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
# （1）将i拆分为j和i-j：j*(i-j)
# （2）将i拆分为j和dp[i-j]：j*dp[i-j]
# 3. 初始化：dp[0]=0 dp[1]=1 dp[2]=1
# 4. 遍历顺序：从左到右
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        if n<=2:
            return 1
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]

        