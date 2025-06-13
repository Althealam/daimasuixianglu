# 1. dp数组以及下标的含义：dp[j]表示背包容量为j的时候，可以获取的最大价值为dp[j]
# 2. 递推公式：
# （1）如果物品i没达到使用上限，并且使用物品i：if cnt[i]<number[i]: dp[j-weight[i]]+value[i]
# （2）不使用物品i：dp[j]
# dp[j]=max(dp[j], dp[j-k*weight[i]]+k*value[i])
# 3. 初始化：dp[j]=0
# 4. 遍历顺序：先物品后背包

c, n = map(int, input().split())
# c表示背包容量，n表示物品数量

weight=list(map(int, input().split(" "))) # 物品重量
value=list(map(int, input().split(" "))) # 物品价格
number=list(map(int, input().split(" "))) # 每个物品的使用上限

dp=[0]*(c+1)
for i in range(n): # 遍历物品
    for j in range(c, weight[i]-1, -1): # 遍历背包，背包为逆序
        for k in range(1, number[i]+1): # 遍历物品的可使用次数
            if k*weight[i]>j: # 当前背包剩余容量无法装入物品i
                break
            else:
                dp[j]=max(dp[j], dp[j-k*weight[i]]+k*value[i])

print(dp[-1])