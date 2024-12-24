# 1. dp数组的定义：dp[i][j]表示的是以i-1为结尾的word1和以j-1为结尾的word2，让这两个字符串相同时需要删除元素的最小次数
# 2. 递推公式：
# if word1[i-1]==word2[j-1]: dp[i][j]=dp[i-1][j-1]
# else: dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+2)（模拟删除元素，因此需要将操作次数+1）
# (1) 删除word1[i-1]:dp[i-1][j]+1
# (2) 删除word2[j-1]:dp[i][j-1]+1
# (3) 删除word1[i-1]和word2[j-1]:dp[i-1][j-1]+2
# 3. 初始化：dp[i][j]可以由dp[i-1][j],dp[i][j-1]和dp[i-1][j-1]推出
# dp[0][j]=j （word2为空字符串，以i-1为结尾的字符串word1要删除多少个元素，才能和word2相同）
# dp[i][0]=i （word1为空字符串，以j-1为结尾的字符串word2要删除多少个元素，才能和word1相同）
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
        # 列为len(word2)+1，行为len(word1)+1
        dp=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        # 初始化
        for i in range(len(word1)+1):
            dp[i][0]=i
        for j in range(len(word2)+1):
            dp[0][j]=j
        # 计算状态转移矩阵
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+2)
        return dp[len(word1)][len(word2)]