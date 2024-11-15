# 多重背包和01背包的区别
# 将多重背包中每个物品摊开则是01背包

# C是背包容量，N是物品
C,N=int().split(" ")
weight=[int(x) for x in input().split(" ")]
values=[int(x) for x in input().split(" ")]
nums=[int(x) for x in input().split(" ")]

dp=[0]*(C+1) # 初始化dp数组


# 遍历物品
for i in range(N):
    # 遍历背包容量（倒叙遍历，因为每个物品只能使用一次，因此必须要倒叙）
    for j in range(C,weights[i]-1,-1):
        for k in range(1,nums[i]+1):
            # 遍历k，如果已经大于背包容量则跳出循环
            if k*weights[i]>j:
                break
            dp[j]=max(dp[j],dp[j-weighs[i]]+values[i])

print(dp[-1])