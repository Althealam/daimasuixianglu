# 1. dp数组以及下标的含义：dp[i][j]表示以s[i-1]为结尾的字符串，和以t[j-1]为结尾的字符串，相同子序列的长度为dp[i][j]
# 如果s是t的子序列，那么dp[len(s)-1][len(t)-1] == len(s)
# 2. 递推公式：
# if s[i-1]==t[j-1]: dp[i][j] = dp[i-1][j-1]+1
# else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# 3. 初始化：dp[i][0] = 0 dp[0][j] = 0

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if dp[-1][-1]==len(s):
            return True
        return False