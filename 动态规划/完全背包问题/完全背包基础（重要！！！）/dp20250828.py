
bagweight=int(input())
weight=list(map(int, input().split()))
value=list(map(int, input().split()))

def ditui(bagweight, weight, value):
    dp=[[0]*(bagweight+1) for _ in range(len(value))]
    for j in range(bagweight+1):
        if j>=weight[0]:
            dp[0][j]=dp[0][j-weight[0]]+value[0]
    
    for i in range(1, len(value)): # 遍历物品
        for j in range(1, bagweight+1):
            if j>=weight[i]:
                dp[i][j]=max(dp[i-1][j], dp[i][j-weight[i]]+value[i])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1][-1]

result=ditui(bagweight, weight, value)
print(result)