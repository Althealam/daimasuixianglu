# 1. dp数组以及下标的含义：
# dp[i][0]表示第i天为持有股票的状态时的最大收益
# dp[i][1]表示第i天为不持有股票的状态时的最大收益
# dp[i][2]表示第i天为当天卖出股票的状态时的最大收益
# dp[i][3]表示第i天为冷冻期的状态时的最大收益
# 2. 递推公式
# dp[i][0]=max(dp[i-1][0], dp[i-1][1]-prices[i], dp[i-1][3]-prices[i])
# dp[i][1]=max(dp[i-1][1], dp[i-1][3])
# dp[i][2]=dp[i-1][0]+prices[i]
# dp[i][3]=dp[i-1][2]
# 3. 初始化：dp[0][0]=-prices[0]
prices = list(map(int, input().split()))

def ditui(prices):
    dp=[[0]*4 for _ in range(len(prices))]
    dp[0][0]=-prices[0]
    for i in range(1, len(prices)):
        dp[i][0]=max(dp[i-1][0], dp[i-1][1]-prices[i], dp[i-1][3]-prices[i])
        dp[i][1]=max(dp[i-1][1], dp[i-1][3])
        dp[i][2]=dp[i-1][0]+prices[i]
        dp[i][3]=dp[i-1][2]
    return max(dp[-1][3], dp[-1][1], dp[-1][2])

result=ditui(prices)
print(result)