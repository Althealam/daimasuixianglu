# 1. definition: dp[i] denotes the least number of perfect square numbers that sum to n
# 2. formula: 
# (1) use num: dp[j-num**2]+1
# (2) don't use num: dp[j]
# 3. initialization: dp=[float('inf')]*(n+1) dp[0]=0
# 4. order: full package（遍历背包的时候不需要进行逆序）, combination number (element first, package then)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[0]=0
        dp[1] = 1
        for num in range(1, n): # iterate elements
            for j in range(num**2, n+1):
                dp[j] = min(dp[j-num**2]+1, dp[j])
        return dp[-1]
