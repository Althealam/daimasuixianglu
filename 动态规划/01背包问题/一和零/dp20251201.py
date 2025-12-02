# 1. definition: dp[i][j] denotes the size of the largest subset of strs which have at most m 0 and n 1
# 2. formula:
# use str: dp[i-zeroNum][j-oneNum]+1
# dp[i][j] = max(dp[i][j], dp[i-zeroNum][j-oneNum]+1)
# 3. initialization: dp = [[0]*(n+1) for _ in range(m+1)]
# 4. order: element first then package, and in the package zero first then one, zero and one should be from right to left

# 为什么这道题0和1需要倒序遍历：i和j都相当于是背包的容量。这道题是01背包，因此我们需要确保物品不会重复取。
# 当是倒序的时候，此时遍历到dp[i][j]，并且dp[i-zeroNum][j-oneNum]还没有被计算过，那么此时s还没有被取过，因此不会出现重复的情况
# 我们希望dp[i-zeroNum][j-oneNum]是第一次取出s，因此需要保持不重复
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)] # m: zero n: one
        for s in strs: # iterate elements
            zeroNum = s.count('0')
            oneNum = s.count('1')
            for i in range(m, -1, -1): # iterate zero
                for j in range(n, -1, -1): # iterate one
                    if i>=zeroNum and j>=oneNum:
                        dp[i][j] = max(dp[i-zeroNum][j-oneNum]+1, dp[i][j])
        return dp[-1][-1]