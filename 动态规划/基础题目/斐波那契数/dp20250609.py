# 1. dp数组以及下标的含义：dp[i]表示第i个斐波那契数
# 2. 递推公式：dp[i]=dp[i-1]+dp[i-2], i>=2
# 3. 初始化：dp[0]=0 dp[1]=1
# 4. 遍历顺序：从左到右遍历

# 读取输入数据
n = int(input())

def ditui(i):
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=1
    for i in range(2, n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]

result=ditui(n)
print(result)

