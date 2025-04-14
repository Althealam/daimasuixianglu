# 1. dp数组以及下标的含义：dp[i][j]表示字符串s在[i,j]范围内最长的回文子序列的长度
# 2. 递推公式：
# （1）s[i]!=s[j]: dp[i][j]=max(dp[i+1][j], dp[i][j-1])
# s[i]不等于s[j]的时候，说明s[i]和s[j]不能同时加入
# （2）s[i]==s[j]: dp[i][j]=dp[i+1][j-1]+2
# s[i]等于s[j]的时候，说明可以同时加入s[i]和s[j]
# 3. 初始化：当i==j的时候，初始化为1，其他初始化为0
# 4. 遍历顺序：dp[i][j]依赖dp[i+1][j-1], dp[i+1][j], dp[i][j-1]
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp=[[0]*len(s) for _ in range(len(s))]

        # 初始化
        for i in range(len(s)):
            for j in range(len(s)):
                if i==j:
                    dp[i][j]=1
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)): # i==j的时候已经初始化了
                if s[i]!=s[j]:
                    dp[i][j]=max(dp[i+1][j], dp[i][j-1])
                else:
                    dp[i][j]=dp[i+1][j-1]+2

        return dp[0][-1]        