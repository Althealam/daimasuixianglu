# 1. dp数组以及下标的含义：dp[i]表示字符串长度为i的时候，如果dp[i]为True表示可以拆分为一个或者多个在字典中出现的单词
# 2. 递推公式：
# dp[i]为True并且[i,j]的子字符串出现在字典里，那么dp[i]为True
# 3. 初始化：全部初始化为False dp[0]=True
# 4. 遍历顺序：本题是求排列数（很容易误会为组合数，但是其实是排列数），因此是先背包后物品（字符串的组合要强调顺序）
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1) # dp[i]表示字符串的前i个字符是否可以由wordDict组成（如果为True则为是）
        dp[0]=True # 初始化（否则后面无法进行递归）
        for j in range(1, len(s)+1): # 遍历背包
            for i in range(j): # 遍历物品（物品必须小于背包的容量才可以）
                if dp[i] and s[i:j] in wordDict:
                    dp[j]=True
        return dp[len(s)]
        