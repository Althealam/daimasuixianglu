# 1. definition: dp[i][j]=True means the substring s[i..j] is palindromic substring
# 2. formula: 
# (1) if s[i]==s[j]: dp[i][j] = dp[i+1][j-1] (in this place, we need to consider i==j and j-i==1)
# (2) if s[i]!=s[j]: dp[i][j] = False
# 3. initialization: dp = [[False]*len(s) for _ in range(len(s))]
# dp[i][i] =True
# 4. order: i first then j, and i is from right to left

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        res = 1
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1,len(s)):
                if s[i]==s[j]:
                    if i==j:
                        dp[i][j]=True
                    elif j-i==1:
                        dp[i][j]=True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False      
                # update result
                if dp[i][j] and j-i+1>=res:
                    res = j-i+1
                    start, end = i, j 
        return s[start:end+1]
        