# 1. definition: dp[i]=True if the s[:i] can be segmented into a space-seperated sequence of one or more dictionary words
# 2. formula: dp[i]=True if s[j, i] in the wordDict and dp[j]=True
# 3. initialization: dp=[False]*(len(s)+1) dp[0]=True
# 4. order: i first then j

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]==True:
                    dp[i]=True 
        return dp[-1]