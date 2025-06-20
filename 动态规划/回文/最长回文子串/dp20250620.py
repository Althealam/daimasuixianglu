# 1. dp数组以及下标的含义：dp[i][j]表示在字符串[i,j]的范围是否是回文子串，如果为True的话表示s[i:j]是回文串，否则的话不是回文串
# 2. 递推公式：
# （1）如果s[i]==s[j]并且dp[i+1][j-1]是回文子串，那么dp[i][j]为True
# （2）如果len(s)<2的话dp[i][j]为True
# （2）否则的话dp[i][j]为False
# 3. 初始化：dp[i][i]=True，全部初始化为False 并且长度为2的s为True
# 4. 遍历顺序：先遍历j，然后再遍历i，并且i一定比j小

# 时间复杂度：O(n**2)，需要填充nxn的dp表格
# 空间复杂度：O(n**2) dp数组
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[False]*len(s) for _ in range(len(s))]

        # 特殊情况判断
        if len(s)<2:
            return s

        max_length = 0
        start, end = 0, 0 # 最长回文子串的起始和结束索引
        for i in range(len(s)): # 初始化
            dp[i][i]=True
        
        for j in range(1, len(s)):
            for i in range(j):
                if s[i]==s[j]:
                    if j-i<2: # 长度为2的情况
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                # 更新最长回文子串
                if dp[i][j]:
                    current_length = j-i+1 # 当前子串的长度
                    if current_length>max_length:
                        max_length = current_length
                        start, end = i, j
        return s[start:end+1]
        