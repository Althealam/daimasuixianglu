# 方法：动态规划（滚动数组）
# 滚动数组相当于将二维数组压缩为一维数组，滚动数组就是将上一层的数组拷贝下来
# 这里的拷贝的含义是：
# 二维数组时：dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
# 一维数组时：dp[i][j]=max(dp[i][j],dp[i][j-weight[i]]+value[i])
# 1. dp数组的含义：dp[j]指的是容量为j的背包所能有的最大价值为bp[j]
# 2. 递推公式：dp[j]=max(dp[j],dp[j-weight[i]]+value[i])
# (1)不放物品i时背包容量为j的最大价值：dp[j]
#（2）放物品i时背包容量为j的最大价值：dp[j-weight[i]]+value[i]
# 3. 初始化：dp[0]表示背包容量为0时的最大价值，因此dp[0]=0
# 4. 遍历顺序：先遍历物品，再遍历背包，并且遍历背包用倒序
# 倒序遍历物品是为了每个物品只被添加一次，如果正序遍历会将物品添加两次
 
n,bagweight=map(int,input().split())
weight=list(map(int,input().split())
value=list(map(int,input().split())

dp=[0]*(bagweight+1)
dp[0]=0 # 背包容量为0，最大价值为0

for i in range(n): # 遍历物品
    for j in range(bagweight,weight[i]-1,-1): # 倒序遍历背包容量j
        dp[j]=max(dp[j],dp[j-weight[i]]+value[i])

print(dp[bagweight])

