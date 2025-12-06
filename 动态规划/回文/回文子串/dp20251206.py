# 1. definition: dp[i][j] means whether the s[i..j] is palindromic substrings, if yes then true, otherwise false
# 2. formula: 
# if s[i]==s[j]:
# (1) i==j: True
# (2) j-i==1: True
# (3) dp[i][j] = dp[i+1][j-1]
# 3. initialization: dp=[[False]*(len(s)+1) for _ in range(len(s)+1)]
# dp[0][0]=True
# 4. order: i+1->i, j-1->j

# 连续回文子串的数量
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*len(s) for _ in range(len(s))]
        dp[0][0] = True
        result = 0 # the number of palindromic substrings
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i]==s[j]:
                    if i==j:
                        dp[i][j]=True
                    elif j-i==1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j]=False
                if dp[i][j]:
                    result+=1
        return result

        
        