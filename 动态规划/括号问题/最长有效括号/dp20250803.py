# 分析：有效的子串一定以)为结尾
# 1. dp数组以及下标的含义：dp[i]表示以下标i字符结尾的最长有效括号的长度 
# 2. 递推公式
# （1）s[i]=')'并且s[i-1]='(：dp[i]=dp[i-2]+2
# （2）s[i]=')'并且s[i-1]=')'
# 如果s[i-dp[i-1]-1]='('，那么dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
# 我们假设倒数第二个')'是一个有效子字符串的一部分，那么对于最后一个')'，如果它是一个更长子字符串的一部分，那么它一定有一个对应的'(' 并且它的位置在倒数第二个')'所在的有效子字符串的前面
# 3. 初始化：全部初始化为0 

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0]*len(s)
        res = 0
        for i in range(len(s)):
            if i>0 and s[i]==')': # 可能遇到了有效的括号对
                if s[i-1]=='(':
                    dp[i]=dp[i-2]+2
                elif s[i-1]==')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                    dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
                res = max(res, dp[i])
        return res