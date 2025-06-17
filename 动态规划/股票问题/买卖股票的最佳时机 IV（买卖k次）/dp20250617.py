# 1. dp数组以及下标的含义：
# （1）dp[i][0]表示第一次持有股票的最大收益
# （2）dp[i][1]表示第一次不持有股票的最大收益
# （3）dp[i][2]表示第二次持有股票的最大收益
# （4）dp[i][3]表示第二次不持有股票的最大收益
# 2. 递推公式：
# 如果j%2==0：dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]-prices[i])
# 如果j%2!=0: dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]+prices[i])
# 3. 初始化：如果j%2==0：dp[i][j]=-prices[0]

k = int(input())
prices = list(map(int, input().split()))

def ditui(k, prices):
    dp=[[0]*2*k for _ in range(len(prices))]
    for j in range(2*k):
        if j%2==0:
            dp[0][j]=-prices[0]
        
    for i in range(1, len(prices)):
        for j in range(2*k):
            if j==0:
                dp[i][j]=max(dp[i-1][j], -prices[i])
            elif j%2==0:
                dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]-prices[i])
            else:
                dp[i][j]=max(dp[i-1][j], dp[i-1][j-1]+prices[i])
    
    return dp[-1][-1]

result=ditui(k, prices)
print(result)
