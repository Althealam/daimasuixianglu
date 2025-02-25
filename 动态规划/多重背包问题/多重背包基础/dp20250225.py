# 1. dp数组以及下标的含义：dp[i]表示当背包容量为i的时候，最多可以放下的物品价值
# 2. 递推公式：
# （1）放k个i：dp[j-weights[i]*k]+values[i]*k
# （2）不放i：dp[j]
# 3. 初始化：dp=[0]*(C+1)
# 4. 遍历顺序：先物品，后背包，最后再遍历每个物品的种类数
C, N=input().split(' ')
C, N=int(C), int(N)

# C：宇航舱的容量，N是矿石的种类数
weights=[int(x) for x in input().split(' ')]
values=[int(x) for x in input().split(' ') if x]
nums=[int(x) for x in input().split(' ')]

dp=[0]*(C+1) # 背包容量
for i in range(N): # 遍历物品
    for j in range(C, weights[i]-1, -1): # 遍历背包
        for k in range(1, nums[i]+1): # 遍历物品
            if k*weights[i]>j:
                break
            dp[j]=max(dp[j], dp[j-weights[i]*k]+values[i]*k)
            
print(dp[-1])