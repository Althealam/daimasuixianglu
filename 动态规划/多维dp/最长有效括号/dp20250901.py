# 1. dp数组以及下标的含义：dp[i]表示以下标i字符结尾的最长有效括号的长度
# 2. 递推公式
# s[i]=')' and s[i-1]='(': dp[i] = dp[i-2]+2
# s[i]=')' and s[i-1]=')'
# 如果s[i-dp[i-1]-1]='('，那么dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
# 3. 初始化：全部初始化为0

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0]*len(s)
        res = 0
        for i in range(len(s)):
            if i>0 and s[i]==')':
                if s[i-1]=='(':
                    dp[i] = dp[i-2]+2
                elif s[i-1]==')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                    dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
                res = max(res, dp[i])
        return res
        