# 1. dp数组的定义：dp[i][j]表示从下标为[0,i]的物品里任意取，放进容量为j的背包里，价值总和最大是多少
# dp[i][j]中，i表示物品，j表示背包容量
# 2. 递推公式：对于dp[i][j]有两种情况，也就是放或者不放
# （1）不放物品i：背包容量为j，里面不妨物品i的最大价值是dp[i-1][j]
# （2）放物品i：背包空出物品i的容量后，背包的容量为j-weight[i]，dp[i-1][j-weight[i]为背包容量为j-weight[i]且不放物品i的最大价值
# dp[i-1][j-weight[i]]+value[i]（物品i的价值）就是背包放物品i得到的最大价值
# 总结：dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])
# 3. dp数组的初始化：
# （1）如果背包容量为0的话，一定有dp[i][0]=0
# （2）dp[0][j]表示的是存放编号为0的物品的时候，各个容量的背包所能存放的最大价值
#      j<weight[0]: dp[0][j]=0
#      j>=weight[0]: dp[0][j]=value[0]
# 3. 遍历顺序
# 有两个遍历的维度：物品与背包重量
# 先遍历物品或者遍历背包都可以，这里我们先遍历物品

# n是物品的种类，bagweight是小明的行李空间
n, bagweight=map(int,input().split())
weight=list(map(int,input().split()))
value=list(map(int,input().split()))
# n=6
# bagweight=1
# weight=[2,2,3,1,5,2]
# value=[2,3,1,5,4,3]

### 初始化
# dp数组是n行m列的，其中n是物品的种类，bagweight是行李空间
dp=[[0]*(bagweight+1) for _ in range(n)] 

# dp[0][j]表示存放编号为0的物品的时候，各个容量的背包所能存放的最大价值
# 当j>=weight[0]的时候，dp[0][j]=value[0]
for j in range(weight[0],bagweight+1):
    dp[0][j]=value[0]

# 递推
for i in range(1,n): # 遍历物品
    for j in range(bagweight+1): # 遍历背包容量
        if j<weight[i]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-weight[i]]+value[i])

print(dp[n-1][bagweight])    
