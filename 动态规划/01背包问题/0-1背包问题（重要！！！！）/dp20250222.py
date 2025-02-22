# 01背包
# 有n件物品和一个最多能背重量为w的背包
# 第i件物品的重量是weight[i]，得到的价值是value[i]
# 每件物品只能使用一次

# 1. dp数组以及下标的含义：dp[i][j]表示从下标为[0,i]的物品里任取，放进容量为j的背包，价值的最大总和为dp[i][j]
# 2. 递推公式：dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
# 3. dp数组的初始化：dp[0][j]表示存放编号为0的物品的时候，各个背包所能存放的最大价值
# （1）j<weight[0]：dp[0][j]=0
# （2）j>=weight[0]：dp[0][j]=value[0]
# dp[i][0]=0
# 4. 遍历顺序：有两个维度：物品和背包重量
# 先遍历物品或者先遍历背包都可以

n, bagweight=map(int, input().split())

weight=list(map(int, input().split()))
value=list(map(int, input().split()))


# 初始化dp数组，dp数组是n（研究材料的种类）行，bagweight（背包容量）列的
# 因为dp[i][j]的i是物品，j是背包容量
dp=[[0]*(bagweight+1) for _ in range(n)]

# 初始化dp[0][j]数组
for j in range(bagweight+1):
    if j<weight[0]:
        dp[0][j]=0
    elif j>=weight[0]:
        dp[0][j]=value[0]

# 遍历物品
for i in range(1,n):
    # 遍历背包
    for j in range(bagweight+1):
        if j<weight[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])

print(dp[n-1][bagweight])            

        