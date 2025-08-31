# 1. dp数组以及下标的含义：dp[i][j]表示以i-1为结尾的word1，和以j-1为结尾的word2，想要达到相等，需要删除元素的步数
# 2. 递推公式：
# word1[i-1]==word2[j-1]: dp[i][j] = dp[i-1][j-1]
# word1[i-1]!=word2[j-1]: 
# (1) dp[i-1][j]+1
# (2) dp[i][j-1]+1
# (3) dp[i-1][j-1]+2
# 3. 初始化：dp[i][0] = i dp[0][j] = j
# 4. 遍历顺序：先遍历word1，再遍历word2
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            dp[i][0] = i
        for j in range(1, len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2)
        return dp[-1][-1]
        