# 1. dp数组以及下标的含义：dp[i][j]表示长度为[0,i-1]的字符串text1和长度为[0,j-1]的字符串text2的最长公共子序列长度为dp[i][j]
# 2. 递推公式：
# （1）text1[i-1]!=text2[j-1]: dp[i][j]=max(dp[i-1][j], dp[i][j-1])
#  (2) text1[i-1]==text2[j-1]: dp[i][j]=dp[i-1][j-1]+1
# 3. 初始化：dp[i][0]=0 dp[0][j]=0 
# 4. 遍历顺序：从前向后，从上到下

# 时间复杂度：O(mn)
# 空间复杂度：O(mn)

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j], dp[i][j-1])
                
        return dp[-1][-1]
        
        