# 动态规划五部曲（统计s中t出现的次数）
# 1. dp数组的含义：以i-1为结尾的s子序列中出现以j-1为结尾的t的个数为dp[i][j]
# 2. 递推公式：
# if s[i-1]==t[j-1]: dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
#   (1) 用s[i-1]来匹配，那么个数为dp[i-1][j-1]
#   (2) 不用s[i-1]来匹配，个数为dp[i-1][j]
# else: dp[i][j]=dp[i-1][j]（s[i-1]与t[j-1]不相等）
# 3. 初始化：
# dp[i][j]可以由dp[i-1][j]和dp[i-1][j-1]推出，因此需要对dp[i][0]和dp[0][j]初始化
# dp[i][0]=1（s中有空字符串的个数为1） dp[0][j]=0（t中有空字符串的个数为0）dp[0][0]=0
# 4. 遍历顺序
# 从左到右，从上到下

# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)):
            dp[i][0]=1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[len(s)][len(t)]
        