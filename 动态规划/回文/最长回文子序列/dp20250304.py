# 回文子串是连续的，而回文子序列可以是不连续的
# 1. dp数组以及下标的含义：dp[i][j]表示字符串s在[i,j]范围内的最长回文子序列的长度为dp[i][j]
# 2. 递推公式
# （1）s[i]==s[j]: dp[i][j]=dp[i+1][j-1]+2
# （2）s[i]!=s[j]: dp[i][j]=max(dp[i+1][j], dp[i][j-1])
# 加入s[j]的回文子序列长度为dp[i+1][j] 加入s[i]的回文子序列长度为dp[i][j-1]
# 3. 初始化：
# （1）i=j: dp[i][j]=1（一个字符的回文子序列长度为1）
# （2）i!=j: dp[i][j]=0
# 4. 遍历顺序：从下到上，从左到右

# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[[0]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i]=1
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)): # 注意j一定是大于i的，并且j是从i+1开始的
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
        