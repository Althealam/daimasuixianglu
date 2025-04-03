C, N=map(int, input().split())
# C是宇航舱的容量，N是矿石的种类数量

weights=[int(x) for x in input().split(' ')]
values=[int(x) for x in input().split(' ') if x]
nums=[int(x) for x in input().split(' ')]


# 1. dp数组以及下标的含义：dp[j]表示宇航舱容量为j的时候，可以容纳的矿石最大价值为dp[j]
# 2. 递推公式：
# （1）不放入物品i：dp[j]
# （2）放入物品i：dp[j-weights[i]*k]+values[i]*k
# 3. 初始化：全部初始化为0
# 4. 遍历顺序：先物品，后背包（逆序），最后遍历该物品的数量
dp=[0]*(C+1) 
for i in range(N): # 遍历物品
    for j in range(C, weights[i]-1, -1): # 遍历背包
        for k in range(nums[i]+1): # 遍历物品容量
            if k*weights[i]>j: # 如果物品i剩下的重要已经超过了背包容量，则跳出循环
                break
            dp[j]=max(dp[j], dp[j-weights[i]*k]+values[i]*k)
print(dp[-1])



