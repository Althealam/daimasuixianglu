# 1. dp[i][j]表示以i-1为结尾的word1，和以j-1为结尾的word2，想要达到相等，所需要删除元素的最小步数
# 2. 递推公式：
# （1）word1[i-1]==word2[j-1]：dp[i][j]=dp[i-1][j-1] 不需要删除 操作次数为0
# （2）word1[i-1]!=word2[j-1]：
# （2.1）只删除word1[i-1]：dp[i-1][j]+1 操作次数为1
# （2.2）只删除word2[j-1]：dp[i][j-1]+1 操作次数为1
# （2.3）同时删除word1[i-1]和word2[j-1]：dp[i-1][j-1]+2 操作次数为2
# 3. 初始化：由递推公式可以知道dp[i][j]是由dp[i][0]和dp[0][j]推导出来的
# （1）dp[i][0]表示以i-1为结尾的word1和空字符串，想要达到相等，所需要删除的最小步数
# dp[i][0]=i
# （2）dp[0][j]表示空字符串和以j-1为结尾的word2，想要达到相等，所需要删除的最小步数
# dp[0][j]=j
# 4. 遍历顺序：先遍历word1，再遍历word2
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            dp[i][0]=i
        for j in range(1, len(word2)+1):
            dp[0][j]=j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2)
        return dp[-1][-1]
        