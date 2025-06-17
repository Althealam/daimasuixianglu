# 1. dp数组以及下标的含义：
# dp[i][0]表示持有股票的最大收益
# dp[i][1]表示不持有股票的最大收益
# 2. 递推公式
# dp[i][0]=max(dp[i-1][0], dp[i-1][1]-prices[i])
# dp[i][1]=max(dp[i-1][1], dp[i-1][0]+prices[i]-fee)
# 3. 初始化：dp[0][0]=-prices[0]


prices = list(map(int, input().split()))
fee = int(input())

def ditui(prices, fee):
    dp=[[0]*2 for _ in range(len(prices))]
    dp[0][0]=-prices[0]

    for i in range(1, len(prices)):
        dp[i][0]=max(dp[i-1][0], dp[i-1][1]-prices[i])
        dp[i][1]=max(dp[i-1][1], dp[i-1][0]+prices[i]-fee)
    
    return dp[-1][1]

result=ditui(prices, fee)
print(result)