prices=list(map(int, input().split()))
def ditui(prices):
    dp=[[0]*2 for _ in range(len(prices))]
    dp[0][0]=-prices[0]

    for i in range(1, len(prices)):
        dp[i][0]=max(dp[i-1][0], dp[i-1][1]-prices[i])
        dp[i][1]=max(dp[i-1][1], dp[i-1][0]+prices[i])
    return dp[-1][1]

result=ditui(prices)
print(result)