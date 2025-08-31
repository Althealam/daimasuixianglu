# 1. dp数组以及下标的含义：dp[i][j]表示以i-1为结尾的s子序列中出现以j-1为结尾的t的个数
# 2. 递推公式
# s[i-1]==t[j-1]: dp[i-1][j]+dp[i-1][j-1]
# s[i-1]!=t[j-1]: dp[i-1][j]
# 3. 初始化：dp[i][0] = 1 dp[0][j] = 1 dp[0][0]=1
# 4. 遍历顺序：先遍历s，再遍历t
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)):
            dp[i][0] = 1
        dp[0][0] = 1
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
                
        