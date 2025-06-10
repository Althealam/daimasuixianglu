# 1. dp数组以及下标的含义：dp[i]表示分拆数字i，可以得到的最大乘积为dp[i]
# 2. 递推公式：dp[i]=max(dp[i], j*(i-j), j*dp[i-j])
# 将i拆分为j和i-j，因此dp[i]可以表示为j*(i-j)或者j*dp[i-j]
# 3. 初始化：dp[0]=0 dp[1]=0 dp[2]=1
# 4. 遍历顺序：从前向后遍历，j需要遍历所有的切割点
n=int(input())

def ditui(n):
    dp=[0]*(n+1)
    dp[2]=1
    for i in range(3, n+1):
        for j in range(1, i):
            dp[i]=max(dp[i], j*(i-j), j*dp[i-j])
    return dp[n]

result=ditui(n)
print(result)