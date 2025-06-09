# 1. dp数组以及下标的含义：dp[i]表示爬到第i个台阶的方法有dp[i]种
# 2. 递推公式：
# dp[i]=dp[i-1]+dp[i-2]
# 3. 初始化：dp[0]=1 dp[1]=1
n=int(input())

def ditui(n):
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2, n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

result=ditui(n)
print(result)