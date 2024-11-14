# 与01背包不同的是，在遍历背包的时候使用正序遍历，而不是用倒序遍历
# 01背包是先遍历物品再遍历背包（一维数组，而完全背包的两个for循环是可以颠倒顺序的

# 方法二：先遍历背包，再遍历物品
def test_CompletePack(weight,value,bagWeight):
    dp=[0]*(bagWeight+1)
    for i in range(bagWeight+1): # 遍历背包
        for j in range(len(weight)): # 遍历物品
            if j-weight[i]>=0:
                dp[j]=max(dp[j],dp[j-weight[i]]+value[i])
    
if __name__=='__main__':
    weight=[1,3,4]
    value=[15,20,30]
    bagWeight=4
    result=test_CompletePack(weight,value,bagWeight)
    print(result)