# 1. dp数组以及下标的含义：dp[j]表示背包容量为j的时候可以获取的最大价值
# 2. 递推公式
# dp[j] = max(dp[j], dp[j-k*weight[i]]+k*value[i])
# 3. 初始化：dp[j] = 0

C, N = map(int, input().split())
weight = list(map(int, input().split()))
price = list(map(int, input().split()))
number = list(map(int, input().split()))

dp = [0]*(C+1)
for i in range(N): # 遍历物品
    for j in range(C, weight[i]-1, -1): # 遍历背包，背包逆序
        for k in range(1, number[i]+1): # 遍历物品的可使用数量
            if k*weight[i]>j:
                break
            else:
                dp[j] = max(dp[j], dp[j-k*weight[i]]+k*value[i])
print(dp[-1])