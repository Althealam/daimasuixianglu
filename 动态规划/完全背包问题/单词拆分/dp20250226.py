# 1. dp数组以及下标的含义：dp[i]表示字符串长度为i的情况下，是否可以拆分为一个或者多个在字典中出现的单词，如果可以的话为True，如果不可以的话为False
# 2. 递推公式：
# 如果dp[j]==True并且[j,i]这个区间在字典中出现了，那么dp[i]=True
# 3. 初始化：dp[0]=True 因为dp[i]需要依靠dp[j]推出来，如果dp[0]为False的话后面无法推出来
# 4. 遍历顺序：本题其实是求组合数，因此是先背包后物品

# 时间复杂度：O(n^2)
# 1. 外层循环：O(len(s))
# 2. 内层循环：O(i)
# 3. 字符切片和集合查找操作：每次都需要对字符串进行切片s[j:i]以及判断该切片是否在集合wordset中
# 字符串切片为O(k)，k是切片的长度；集合查找的操作s[j:i] in wordSet的时间复杂度为O(1)

# 空间复杂度：O(n)
# 1. 集合wordSet：O(m)，m代表的是单词列表中不同单词的数量
# 2. dp数组：O(n)

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str 非空字符串
        :type wordDict: List[str] 单词列表
        :rtype: bool
        """
        wordSet=set(wordDict) # 这里弄成set主要是为了后续s[j:i] in wordSet优化查询效率
        dp=[False]*(len(s)+1) # dp[i]表示字符串的前i个字符是否可以被拆分为单词
        dp[0]=True # 第一个必须初始化为True，否则后面的推导都为False

        for i in range(1, len(s)+1): # 遍历背包
            for j in range(i): # 遍历单词
                if dp[j] and s[j:i] in wordSet:
                    dp[i]=True
                    break
        return dp[len(s)]