# 注意：本题相当于是在s中删除字符
# 1. dp数组以及下标的含义：dp[i][j]表示以i-1为结尾的s子序列中出现以j-1为结尾的t的个数为dp[i][j]
# 2. 递推公式
# （1）s[i-1]==t[j-1]：
# （1.1）用s[i-1]来匹配：dp[i-1][j-1]
# （1.2）不用s[i-1]来匹配：dp[i-1][j]
# 比如：s为bagg，t为bag，其中s[3]和t[2]是相同的，但是字符串s可以不用s[3]来匹配，即用s[0]s[1]s[2]来组成bag
# dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
# （2）s[i-1]!=t[j-1]：dp[i-1][j]
# 3. 初始化：由递推公式可以知道dp[i][j]是由dp[i-1][j]和dp[i][j-1]推导出来的
# dp[i][0]表示以i-1为结尾的s子序列中出现空字符串的个数 dp[i][0]=1（将s中的字符全部删完即可）
# dp[0][j]表示空字符串中出现以j-1为结尾的t的个数 dp[0][j]=0
# dp[0][0]表示空字符串中出现空字符串的个数 dp[0][0]=1
# 4. 遍历顺序：先遍历s，再遍历t

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)):
            dp[i][0]=1
        dp[0][0]=1
        for i in range(1, len(s)+1): # 遍历s
            for j in range(1, len(t)+1): # 遍历t
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
        