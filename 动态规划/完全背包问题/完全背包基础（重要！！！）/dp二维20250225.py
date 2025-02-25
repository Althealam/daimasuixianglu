# 1. dp数组以及下标的含义：dp[i][j]表示从下标[0,i]的物品中抽取，每个物品可取无限次，放进容量为j的书包，求最大价值和
# 2. 递推公式：
# （1）j>weight[i]: dp[i][j]=max(dp[i-1)[j], dp[i][j-weight[i]+value[i])
# （2）j<weight[i]: dp[i][j]=dp[i-1][j]
# 3. 初始化：
# dp[0][j]：当j>weight[0]时，dp[0][j]=dp[0][j-weight[0]+values[0]
# dp[i][0]=0
# 4. 遍历顺序：先物品后背包

n, bagweight=map(int, input().split())
weight=[]
value=[]
for _ in range(n):
    w,v=map(int, input().split())
    weight.append(w)
    value.append(v)

dp=[[0]*(bagweight+1) for _ in range(n)]
# 初始化dp数组
for j in range(weight[0], bagweight+1):
    dp[0][j]=dp[0][j-weight[0]]+value[0]

# 动态规划
for i in range(1, n): # 遍历物品
    for j in range(bagweight+1): # 遍历背包
        if j<weight[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-weight[i]]+value[i])

print(dp[n-1][bagweight])