# 1. dp数组以及下标的含义：dp[i]表示0到i-1的单词范围内是否可以由wordDict中的多个单词组成
# 2. 递推公式
# dp[i]=True if s[i:j]在wordDict中并且dp[j]=True
# 3. 初始化：全部初始化为False dp[0] = True
# 4. 遍历顺序：先j后i
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True
        for j in range(1, len(s)+1):
            for i in range(j):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]
        