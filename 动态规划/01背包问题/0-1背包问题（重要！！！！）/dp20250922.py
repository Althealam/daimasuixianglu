# 1. dp数组以及下标的含义：dp[j]表示背包容量为j的时候可以放入的最大价值为dp[j]
# 2. 递推公式：
# dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
# 3. 初始化：dp[0] = 0
# 4. 遍历顺序：先物品后背包 背包逆序（01背包）
m, n = map(int, input().split())

weight = list(map(int, input().split()))
value = list(map(int, input().split()))

dp = [0]*(n+1)
for i in range(m): # 遍历物品
    for j in range(n, -1, -1): # 遍历背包
        if j>=weight[i]:
            dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
print(dp[n])

