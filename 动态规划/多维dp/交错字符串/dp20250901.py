# 1. dp数组以及下标的含义：dp[i][j]表示s1的前面i个字符和s2的前面j个字符是否能构成s3的前面i+j个字符
# 2. 递推公式
# （1）len(s1)+len(s2)!=len(s3): False
# （2）dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]: s1的前面i个字符可以构成s3的前面i个字符
# （3）dp[0][j] = dp[0][j-1] and s2[j-1]==s3[j-1]: s2的前面j位字符可以构成s3的前面j个字符
# （4）dp[i][j] = (dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1]) s1前面i位和s2前面j位能否组成s3的前面i+j位
# 3. 初始化：dp[0][0] = True 全部初始化为False
# dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]
# dp[0][j] = dp[0][j-1] and s2[j-1]==s3[j-1]
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp=[[False]*(len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0]=True
        if len(s1)+len(s2)!=len(s3):
            return False
        for i in range(1, len(s1)+1):
            dp[i][0] = (dp[i-1][0] and s1[i-1]==s3[i-1])
        for j in range(1, len(s2)+1):
            dp[0][j] = (dp[0][j-1] and s2[j-1]==s3[j-1])
        
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                dp[i][j] = (dp[i][j-1] and s2[j-1]==s3[i+j-1]) or (dp[i-1][j] and s1[i-1]==s3[i+j-1])
        return dp[-1][-1]
