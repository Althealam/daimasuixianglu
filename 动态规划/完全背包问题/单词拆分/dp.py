# 完全背包问题，其中wordDict是物品，s是背包，可以将本题理解成可否将物品组合成背包
# 动态规划五部曲
# 1. dp数组的含义：字符串长度为i的话，dp[i]为true，表示可以拆分为一个或者多个在字典中出现的单词
# 2. 递推公式：
# dp[j]=True，并且[j,i]这个区间的子串出现在字典里，那么dp[i]=True
# 由此 if([j,i]这个区间的子串常出现在字典里&&dp[j]=True)，那么dp[i]=True
# 3. 初始化：dp[i]的状态依靠dp[j]是否是true，dp[0]=True
# 4. 确定遍历顺序：本题是求排列数，因此是先遍历背包，后遍历物品
# （1）求组合数就是外层for循环遍历物品，内层for循环遍历背包
# （2）求排列数就是外层for循环遍历背包，内层for循环遍历物品

# 时间复杂度：
# 1. 外层循环：i从1遍历到n，其中n是字符串s的长度
# 2. 内层循环：对于每一个i，内层循环遍历j从0到i-1
# 3. 检查子串是否在wordSet中：O(1)
# 总的时间复杂度：O(nxn)
# 空间复杂度：
# 1. wordSet：将wordDict转换为集合wordSet，需要O(k)的空间，其中k是wordDict中的单词数量
# 2. dp数组：dp数组长度为n+1，用于存储到每个位置的拆分状态，因此需要O(n)的空间
# 总的空间复杂度：O(n+k)（n是字符串s的长度，k是字典wordDict中的单词数量）

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet=set(wordDict)
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True # 初始状态，空字符串可以被拆分成单词

        for i in range(1,n+1): # 遍历背包
            for j in range(i): # 遍历单词
                if dp[j] and s[j:i] in wordSet:
                    dp[i]=True # 如果s[0:j]可以被拆分为单词， 并且s[j:i]在单词集合中存在，则s[0:i]可以被拆分为单词
                    break
        return dp[n]
        