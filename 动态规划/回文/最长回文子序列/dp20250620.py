# 1. dp数组以及下标的含义：dp[i][j]表示区间[i,j]范围内的最长回文子序列的长度为dp[i][j]
# 2. 递推公式：
# （1）s[i]==s[j]: dp[i][j]=dp[i+1][j-1]+2
# （2）s[i]!=s[j]: dp[i][j]=max(dp[i+1][j], dp[i][j-1])
# 3. 初始化：全部初始化为0 dp[0][0]=1 dp[i][i]=1
# 4. 遍历顺序：从下到上 从左到右

s = str(input())

def ditui(s):
    dp=[[0]*(len(s)) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i]=1
    
    for i in range(len(s)-1, -1, -1):
        for j in range(i+1, len(s)):
            if s[i]==s[j]:
                dp[i][j]=dp[i+1][j-1]+2
            else:
                dp[i][j]=max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][-1]


result=ditui(s)
print(result)