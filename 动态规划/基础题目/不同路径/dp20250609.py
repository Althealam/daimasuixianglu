# 1. dp数组以及下标的含义：dp[i][j]表示从(0,0)出发到(i,j)总共有dp[i][j]条不同路径
# 2. 递推公式：dp[i][j]=dp[i-1][j]+dp[i][j-1]
# 3. 初始化：dp[0][0]=1 dp[i][0]=1 dp[0][j]=1
# 4. 遍历顺序：从上到下，从左到右


# m行n列
m, n = map(int, input().split())

def ditui(m, n):
    dp=[[0]*n for _ in range(m)] # m行n列

    # 初始化
    for i in range(m):
        dp[i][0]=1
    for j in range(n):
        dp[0][j]=1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
    return dp[-1][-1]

result=ditui(m, n)
print(result)