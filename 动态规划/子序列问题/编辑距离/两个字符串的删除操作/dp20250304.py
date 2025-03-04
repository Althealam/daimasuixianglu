# 1. dp数组以及下标的含义：dp[i][j]表示以i-1为结尾的字符串word1，和以j-1为结尾的字符串word2，想要达到相等，需要删除元素的最少次数；
# 2. 递推公式：
# （1）word1[i-1]==word2[j-1]：dp[i][j]=dp[i-1][j-1]
# （2）word1[i-1]!=word2[j-1]: min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2)
# （2.1）删除word1[i-1]，最少操作次数为dp[i-1][j]+1
# （2.2）删除word2[j-1]，最少操作次数为dp[i][j-1]+1
# （2.3）同时删除word1[i-1]和word2[j-1]，最少操作次数为dp[i-1][j-1]+2
# 3. 初始化：需要初始化dp[i][0]和dp[0][j] 并且dp[i][0]=i dp[0][j]=j
# 4. 遍历顺序：从上到下，从左到右

# 时间复杂度：O(mn)，其中m是word1的字符串长度，n是word2的字符串长度
# 空间复杂度：O(mn)
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0]=i

        for j in range(len(word2)+1):
            dp[0][j]=j
        
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j-1]+2, dp[i-1][j]+1, dp[i][j-1]+1)
        
        return dp[-1][-1]