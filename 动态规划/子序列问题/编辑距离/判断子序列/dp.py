# 分析：从t里面删除字符，查看是否有s在t中（编辑距离类）
# 1. dp数组：dp[i][j]表示的是以i-1为结尾的字符串s和以j-1结尾的字符串t的相同子序列的长度
# 2. 递推公式：
# if s[i-1]==t[j-1]: dp[i][j]=dp[i-1][j-1]+1
# else: dp[i][j]=dp[i][j-1]
# 3. 初始化：
# dp[i][j]可以由dp[i][j-1]和dp[i-1][j-1]推导出来
# dp[i][0]和dp[0][j]需要进行初始化，dp[i][0]=dp[0][j]=0
# 4. 遍历顺序：
# 从左到右，从上到下

# 时间复杂度:O(n^2)
# 空间复杂度:O(n^2)

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=dp[i][j-1]
        if dp[len(s)][len(t)]==len(s):
            return True
        return False
        