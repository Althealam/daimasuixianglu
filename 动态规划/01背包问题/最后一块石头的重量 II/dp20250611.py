# 1. dp数组以及下标的含义：dp[j]表示容量为j的背包，最多可以装的最大价值为dp[j]
# 2. 递推公式：
# （1）不装入石头i：dp[j]
# （2）装入石头i：dp[j-stones[i]]+stones[i]
# dp[j]=max(dp[j], dp[j-stones[i]]+stones[i])
# 3. 初始化：最大容量是所有石头的重量和，也就是30*1000=30000
# 4. 遍历顺序：先遍历物品，后遍历背包，背包需要逆序
# 最后返回的结果是sum(stones)-2*dp[sum(stones)//2]

stones=list(map(int, input().split()))

def ditui(stones):
    dp=[0]*15001
    total_sum=sum(stones)
    target=total_sum//2

    for stone in stones: # 遍历物品
        for j in range(target, -1, -1): # 遍历背包
            if j>=stone:
                dp[j]=max(dp[j], dp[j-stone]+stone)
    return total_sum-2*dp[target]
result=ditui(stones)
print(result)