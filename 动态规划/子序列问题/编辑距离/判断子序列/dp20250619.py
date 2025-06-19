# 1. dp数组以及下标的含义：dp[i][j]表示以i-1为结尾的字符串s和以j-1为结尾的字符串t的相同子序列的长度
# 2. 递推公式
# （1）s[i-1]==t[j-1]: dp[i][j]=dp[i-1][j-1]+1
# （2）s[i-1]!=t[j-1]: dp[i][j]=max(dp[i-1][j], dp[i][j-1])
# 3. 初始化：全部初始化为0
# 4. 遍历顺序：先遍历s再遍历t，从左到右从上到下
# 当dp[-1][-1]=len(s)时，说明s是t的子序列
s=str(input())
t=str(input())

def ditui(s, t):
    dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1]==t[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j], dp[i][j-1])
    if dp[-1][-1]==len(s):
        return True
    return False