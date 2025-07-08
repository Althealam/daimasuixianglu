# 1. dp数组以及下标的含义：dp[i][j]表示s在[i,j]的范围内是否是回文子串，如果为True的话则表示是
# 2. 递推公式：
# s[i]==s[j]: dp[i][j] = dp[i+1][j-1]
# s[i]!=s[j]: dp[i][j] = False
# 3. 初始化：全部初始化为False dp[i][i]=True
# 4. 遍历顺序：j一定比i大，因此先遍历j再遍历i
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i]=True
        
        max_length = 0 # 回文子串的最长长度
        start, end = 0, 0 # 标记最长回文子串的开始和结束为止
        for j in range(len(s)):
            for i in range(j):
                if s[i]==s[j]:
                    if j-i<2:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                if dp[i][j]:
                    current_length = j-i+1
                    if current_length>max_length:
                        max_length = current_length
                        start, end = i, j
        return s[start:end+1]