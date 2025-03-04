# 1. dp数组以及下标的含义：dp[i][j]表示以i-1为结尾的word1，和以j-1为结尾的word2，最近编辑距离为dp[i][j]
# 2. 递推公式：
# （1）word1[i-1]==word2[j-1]: dp[i][j]=dp[i-1][j-1] 不需要做任何的编辑
# （2）word1[i-1]!=word2[j-1]: dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
# （2.1）word1删除一个元素 dp[i][j]=dp[i-1][j]+1
# （2.2）word2删除一个元素：dp[i][j]=dp[i][j-1]+1（word2删除一个元素，相当于word1添加一个元素）
# （2.3）替换元素：dp[i][j]=dp[i-1][j-1]+1
# 3. 初始化：dp[i][0]=i dp[0][j]=j
# 4. 遍历顺序：从左到右，从上到下

# 时间复杂度：O(mn)
# 空间复杂度：O(mn)

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp=[[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        for i in range(len(word2)+1):
            dp[i][0]=i
        for j in range(len(word1)+1):
            dp[0][j]=j
        for i in range(1, len(word2)+1):
            for j in range(1, len(word1)+1):
                if word2[i-1]==word1[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        return dp[-1][-1]
        