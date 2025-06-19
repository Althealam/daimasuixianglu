# 1. dp数组以及下标的含义：dp[i][j]表示以i-1为结尾的s子序列出现以j-1为结尾的t子序列的次数为dp[i][j]
# 2. 递推公式：
# （1）s[i-1]==t[j-1]
# （1.1）用s[i-1]来匹配：dp[i-1][j-1]
# （1.2）不用s[i-1]来匹配：dp[i-1][j]
# dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
# （2）s[i-1]!=t[j-1]: dp[i-1][j]
# 3. 初始化：全部初始化为0
# dp[i][0]=1（将s中的字符串全部删完即可）
# dp[0][j]=0
# 4. 遍历顺序：先遍历s，再遍历t
s= str(input())
t = str(input())

def ditui(s, t):
    dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]
    for i in range(len(s)+1):
        dp[i][0]=1
    
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]

    return dp[-1][-1]

result=ditui(s, t)
print(result)