# 1. dp数组以及下标的含义：dp[i][j]表示以word1[i-1]为结尾的字符串要变成以word2[j-1]的字符串需要的最少操作数
# 2. 递推公式
# （1）删除word1[i-1]的一个字符/增加word2[j-1]的一个字符：dp[i-1][j]+1
# （2）不需要变化：word1[i-1]==word2[j-1]: d[i-1][j-1]
# （3）替换：dp[i-1][j-1]+1
# 3. 初始化：dp[i][0] = i dp[0][j] = j
# 4. 遍历顺序：先word1后word2
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for j in range(len(word2)+1):
            dp[0][j] = j
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        return dp[-1][-1]
        