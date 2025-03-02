# 本题相当于：有几种方式删除s中的元素，可以让s变成t（s是长序列，t是短序列）
# 1. dp数组以及下标的含义：以i-1为结尾的s子序列中出现以j-1为结尾的t的个数为dp[i][j]
# 2. 递推公式：
# （1）s[i-1]==t[j-1]: dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
# 考虑使用s[i-1]则为dp[i-1][j-1] 不使用s[i-1]则为dp[i-1][j]
# 由于是考虑s中有多少个t，因此只考虑删除s，而不考虑删除t
# （2）s[i-1]!=t[j-1]: dp[i][j]=dp[i-1][j]
# 3. 初始化：需要初始化第一行和第一列 
# （1）dp[i][0]=1 相当于将s中的元素全部删掉可以得到空字符串t，也就是有1种方法，即删除掉所有的元素
# （2）dp[0][j]=0 相当于t的[0,j]字符串在空字符串中永远无法得到
# （3）dp[0][0]=1 相当于s不需要做任何改动，就可以得到空字符串
# 4. 遍历顺序：从上到下 从左到右

# 时间复杂度：O(mn)
# 空间复杂度：O(mn)

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0]=1
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
        