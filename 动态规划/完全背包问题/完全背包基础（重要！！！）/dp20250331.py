# 1. dp数组以及下标的含义：dp[i][j]表示从0到i的物品里选择，装满容量为j的背包，背包的最大价值为dp[i][j]
# 2. 递推公式：
# （1）不放物品i：dp[i-1][j]
# （2）放物品i：dp[i][j-weight[i]]+value[i]
# dp[i][j]=max(dp[i-1][j], dp[i]-weight[i])+value[i]
# 3. 初始化：
# （1）dp[0][j]：当j<weight[0]的时候，dp[0][j]=0；当j>weight[0]的时候，dp[0][j]=value[0]
# （2）dp[i][0]=0
# 4. 遍历顺序：先物品后背包

# 处理输入
n, bag_weight=map(int, input().split())
weight=[]
value=[]
for _ in range(n):
    w, v=map(int, input().split())
    weight.append(w)
    value.append(v)


def wanquanbeibao(n, bag_weight, weight, value):
    """
    完全背包解法
    """
    dp=[[0]*(bag_weight+1) for _ in range(n)]

    for j in range(weight[0], bag_weight+1):
        dp[0][j]=dp[0][j-weight[0]]+value[0]

    for i in range(1, n): # 遍历物品
        for j in range(1, bag_weight+1): # 遍历背包
            if j<weight[i]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=max(dp[i-1][j], dp[i][j-weight[i]]+value[i])

    return dp[n-1][bag_weight]

print(wanquanbeibao(n, bag_weight, weight, value))