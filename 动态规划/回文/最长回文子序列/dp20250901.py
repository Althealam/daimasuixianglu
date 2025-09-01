# 1. dp数组以及下标的含义：dp[i][j]表示区间[i+1, j-1]内的最长回文子串的长度
# 2. 递推公式：
# （1）s[i]==s[j]: dp[i][j] = dp[i+1][j-1]+2
# （2）s[i]!=s[j]: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
# 3. 初始化：dp[0][0]=1 dp[i][i]=1
# 4. 遍历顺序：i到序遍历 
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i]==s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
        