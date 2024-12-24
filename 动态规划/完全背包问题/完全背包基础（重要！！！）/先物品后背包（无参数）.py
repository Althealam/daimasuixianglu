# 与01背包不同的是，在遍历背包的时候使用正序遍历，而不是用倒序遍历
# 01背包是先遍历物品再遍历背包（一维数组，而完全背包的两个for循环是可以颠倒顺序的

# 方法一：先遍历物品，再遍历背包
def test_CompletePack():
    weight=[1,3,4]
    value=[15,20,30]
    bagWeight=4
    dp=[0]*(bagWeight+1)
    for i in range(len(weight)): # 遍历物品
        for j in range(weight[i],bagWeight+1): # 遍历背包容量
            dp[j]=max(dp[j],dp[j-weight[i]]+value[i])
    print(dp[bagWeight])

test_CompletePack()