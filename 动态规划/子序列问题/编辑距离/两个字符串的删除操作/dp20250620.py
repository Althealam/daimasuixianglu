# 1. dp数组以及下标的含义：dp[i][j]表示以i-1为结尾的字符串word1和以j-1为结尾的字符串word2要达到相等，所需要删除的字符次数为dp[i][j]
# 2. 递推公式：
# （1）word1[i-1]==word2[j-1]: dp[i][j]=dp[i-1][j-1]
# （2）word1[i-1]!=word2[j-1]: 
# （2.1）删除word1[i-1]：dp[i][j]=dp[i-1][j]+1
# （2.2）删除word2[j-1]: dp[i][j]=dp[i][j-1]+1
# （2.3）同时删除word1[i-1]和word2[j-1]：dp[i][j]=dp[i-1][j-1]+2
# dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2)
# 3. 初始化：dp[0][0]=0 dp[i][0]=i dp[0][j]=j
# 4. 遍历顺序：先遍历word1再遍历word2
word1 = str(input())
word2 = str(input())

def ditui(word1, word2):
    dp=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
    dp[0][0]=0

    # 初始化
    for i in range(len(word1)+1):
        dp[i][0]=i
    for j in range(len(word2)+1):
        dp[0][j]=j

    # 递推
    for i in range(1, len(word1)+1):
        for j in range(1, len(word2)+1):
            if word1[i-1]==word2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2)
    print(dp)
    return dp[-1][-1]

result=ditui(word1, word2)
print(result)