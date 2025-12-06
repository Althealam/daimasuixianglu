# 1. definition: dp[i][j] is the minimum number of steps required to make word1 (end with word1[i-1]) and word2 (end with word2[j-1]) the same
# 2. formula
# if word1[i-1]==word2[j-1]: dp[i][j] = dp[i-1][j-1]
# elif word1[i-1]!=word2[j-1]: dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2)
# 3. initialization: dp[i][0] = i dp[0][j] = j
# we have to define the dp as [[0]*(len(word2)+1) for _ in range(len(word1)+1)], otherwise there will be a problem in the initialization
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