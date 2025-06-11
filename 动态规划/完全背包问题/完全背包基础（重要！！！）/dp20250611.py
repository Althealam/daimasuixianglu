# 1. dp数组以及下标的含义：dp[i][j]表示从[0, i]的物品里选取，每个物品可以选取无限次，装满容量为j的背包，价值总和最大为dp[i][j]
# 2. 递推公式
# （1）不放入物品i：dp[i-1][j]
# （2）放入物品i：dp[i][j-weight[i]]+value[i]
# dp[i][j]=max(dp[i-1][j], dp[i][j-weight[i]]+value[i])
# 注意：如果是物品只能取一次，那么就是dp[i-1][j-weight[i]]+value[i]
# 3. 初始化：全部初始化为0
# dp[0][j]当j>=weight[0]的时候dp[0][j]=dp[0][j-weight[0]]+value[0] dp[0][j]= dp[i][0]=0
# 4. 遍历顺序：先物品后背包

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