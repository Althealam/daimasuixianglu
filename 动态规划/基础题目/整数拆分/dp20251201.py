# 1. definition of dp: dp[i] denotes the maximal product of integers
# 2. formula:
# (1) dp[i] = j*(i-j)
# (2) dp[i] = j*dp[i-j]
# dp[i] = max(j*(i-j), j*dp[i-j])
# 3. initialization: dp[0] = 0 dp[1] = 0 dp[2] = 1
# 4. order: i first, then j
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0]=0
        dp[1]=0
        if n<2:
            return dp[n]
        dp[2]=1
        for i in range(3, n+1): # i first
            for j in range(1, i): # iteration the component of j and i-j
                dp[i] = max(j*(i-j), j*dp[i-j], dp[i])
        return dp[-1]

        