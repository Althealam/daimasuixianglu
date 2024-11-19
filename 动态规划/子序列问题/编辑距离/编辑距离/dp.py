# 三种操作：添加元素、删除元素、替换元素
# 1. dp数组：以i-1为结尾的word1和以j-1为结尾的word2，最少的操作次数为dp[i][j]
# 2. 递推公式：
# if word1[i-1]==word2[j-1]: dp[i][j]=dp[i-1][j-1]
# else: dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
# (1) 删除word1的i-1: dp[i-1][j]+1（删除word1的i-2的元素，其实和添加word2的i-1是一样的，操作次数是一致的）
# (2) 删除word2的j-1: dp[i][j-1]+1（删除word2的j-2的元素，也就是以下标i-1为结尾，j-2为结尾的word2的最近编辑距离）
# (3) 替换元素，word1替换word1[i-1]，使其与word2[j-1]相同，此时不用增加删除元素: dp[i-1][j-1]+1
# 3. 初始化：dp[i][j]可以由dp[i-1][j],dp[i][j-1],dp[i-1][j-1]推出
# 需要初始化dp[0][j]和dp[i][0]
# dp[i][0]=i, dp[0][j]=j
# 4. 遍历顺序：从左到右，从上到下

# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)

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
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)
        return dp[len(word1)][len(word2)]