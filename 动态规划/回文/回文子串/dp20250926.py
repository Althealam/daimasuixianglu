# 1. dp数组以及下标的含义：dp[i][j]表示下标为i到j的字符串是否为回文子串，如果是的话则为True，否则为False
# 2. 递推公式
# （1）s[i]!=s[j]: False
# （2）s[i]==s[j]：
# i==j: True
# abs(i-j)==1: True
# abs(i-j)>1: dp[i][j] = dp[i+1][j-1]
# 3. 初始化：全部初始化为False dp[0][0]=True

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*len(s) for _ in range(len(s))]
        dp[0][0] = True
        result = 0
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i]==s[j]:
                    if i==j:
                        dp[i][j] = True
                    elif j-i==1:
                        dp[i][j]=True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    result+=1
        return result