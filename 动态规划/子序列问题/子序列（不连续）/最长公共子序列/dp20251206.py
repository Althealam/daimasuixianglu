# 1. definition: dp[i][j] is the length of their longest common subsequence when ends with text1[i-1] and text2[j-1]
# 2. formula:
# if text1[i-1]==text2[j-1]: dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j])
# else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# 3. initialization: dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
# 4. order: text1 first then text2
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        res = 0
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                res = max(res, dp[i][j])
        return res

        