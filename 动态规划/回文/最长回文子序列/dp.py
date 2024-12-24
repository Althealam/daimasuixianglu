# 1. dp数组：字符串s在[i,j]的范围内最长的回文子序列长度为dp[i][j]（上一题是回文子串，本题是回文子序列）
# 2. 递推公式：（在回文子串的题目中，关键逻辑在于判断s[i]和s[j]是否相同）
# if s[i]==s[j]: dp[i][j]=dp[i+1][j-1]+2
# else: dp[i][j]=max(dp[i][j-1],dp[i+1][j])
# 如果s[i]!=s[j]，说明s[i]和s[j]的同时加入，并不能增加[i,j]区间的回文子序列的长度，那么分别加入s[i]和s[j]，看看哪一个可以组成最长的回文子序列
# （1）加入s[j]的回文子序列长度为dp[i+1][j]
# （2）加入s[i]的回文子序列长度为dp[i][j-1]
# 因此将dp[i][j]取最大的，即dp[i][j]=max(dp[i+1][j],dp[i][j-1])
# 3. 初始化：i从左往右移动，j从右往左移动
# 当i=j时，dp[i][j]=1；当i不等于j的时候，dp[i][j]=0
# 4. 遍历顺序：dp[i][j]可以由dp[i][j-1], dp[i+1][j], dp[i+1][j-1]推出
# 因此遍历顺序为从下往上遍历，从左往右遍历（一定要先遍历i，再遍历j，因为j一定是大于等于i的，因此j是依赖于i的）

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
        for i in range(len(s)-1,-1,-1): # 行的遍历是从下到上
            for j in range(i+1,len(s)): # 列的遍历是从左到右，并且j>=i
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i+1][j])
        return dp[0][len(s)-1]
        