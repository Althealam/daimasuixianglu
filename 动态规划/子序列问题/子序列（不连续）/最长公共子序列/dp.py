# 最长公共子序列的元素之间可以不连续
# 1. dp数组：dp[i][j]表示长度为[0,i-1]的字符串text1和长度为[0,j-1]的字符串text2的最长公共子序列为dp[i][j]
# 2. 递推公式：
# if nums1[i-1]==nums2[j-1]: dp[i][j]=dp[i-1][j-1]+1
# else: dp[i][j]=max(dp[i-1][j],dp[i][j-1])
# 3. 初始化
# 由递推公式可以知道,dp[i][j]可以由dp[i-1][j],dp[i][j-1],dp[i-1][j-1]推出
# dp[i][0]与dp[0][j]都是0（相当于求和空字符串的最长公共子序列）
# 4. 遍历顺序
# 从左到右，从上到下

# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[len(text1)][len(text2)]

        