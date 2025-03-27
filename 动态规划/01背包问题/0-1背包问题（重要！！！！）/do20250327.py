# 1. dp数组以及下标的含义：dp[i][j]表示从[0,i]的物品里选取，装满容量为j的背包，小明能够携带的研究材料的最大价值为dp[i][j]
# 2. 递推公式：
# （1）不放入物品i：dp[i-1][j]
# （2）放入物品i：dp[i-1][j-weight[i]]+value[i]
# dp[i][j]=max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
# 3. 初始化：dp[0][0]=0
# 4. 遍历顺序：从左到右，从上到下

n, bagweight=map(int, input().split()) 
# n表示研究材料的种类，bagweight表示小明的行李空间

weight=list(map(int, input().split()))
value=list(map(int, input().split()))

# dp数组是n行bagweight列（行是研究材料的种类，列是行李空间容量）
dp=[[0]*(bagweight+1) for _ in range(n)]

for i in range(n):
    for j in range(bagweight+1):
        # 无法放下第i个物品
        if j<weight[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])

print(dp[n-1][bagweight])