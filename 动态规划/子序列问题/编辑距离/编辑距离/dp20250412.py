# 1. dp数组以及下标的含义：dp[i][j]表示以i-1为结尾的word1和以j-1为结尾的word2，要将word1变成word2的最少操作数
# 2. 递推公式：
# （1）word1[i-1]=word2[j-1]：dp[i-1][j-1]（不做操作）
# （2）word1[i-1]!=word2[j-1]：
# （2.1）word1删除一个元素：dp[i-1][j]+1
# （2.2）word2删除一个元素：dp[i][j-1]+1
# 注意：删除元素其实就是添加元素（word1删除一个元素，其实就是word2添加一个元素）
# （2.3）替换word1[i-1]/替换word2[j-1]：dp[i-1][j-1]+1 
# 3. 初始化：dp[i][j]都是由dp[i][0]和dp[0][j]推导出来的
# dp[i][0]表示以i-1为结尾的字符串变成空字符串的最小操作数为i
# dp[0][j]表示以j-1为结尾的字符串要变成空字符串的最小操作数为j
# 4. 遍历顺序：先遍历word1，再遍历word2
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for i in range(1, len(word1)+1):
            dp[i][0]=i
        for j in range(1, len(word2)+1):
            dp[0][j]=j
        for i in range(1, len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
        return dp[-1][-1]
        