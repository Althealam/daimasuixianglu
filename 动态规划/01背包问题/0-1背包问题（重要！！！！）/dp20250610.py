# 1. dp数组以及下标的含义：dp[i][j]表示从下标为0到i的物品中选取，放进容量为j的背包，价值最大为dp[i][j]
# 2. 递推公式：
# （1）放入物品i：dp[i][j-weight[i]]+value[i]
# （2）不放入物品i：dp[i-1][j]
# dp[i][j]=max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
# 3. 初始化：dp[i][0]=0 dp[0][j]=value[0](j>=weight[0])
# 4. 遍历顺序：先物品后背包，从前向后遍历

n, bagweight = map(int, input().split())
# m表示研究材料的种类，n表示小明的行李空间

weight=list(map(int, input().split())) # 研究材料所占用的空间
value=list(map(int, input().split())) # 每种研究材料的价值


def ditui(n, bagweight, weight, value):
    # i是物品，j是背包容量
    dp=[[0]*(bagweight+1) for _ in range(n)]
    for j in range(bagweight+1):
        if j>=weight[0]:
            dp[0][j]=value[0]
    
    for i in range(1, n): # 遍历物品
        for j in range(bagweight+1): # 遍历背包
            if j<weight[i]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])

    return dp[-1][-1]
result=ditui(n, bagweight, weight, value)
print(result)