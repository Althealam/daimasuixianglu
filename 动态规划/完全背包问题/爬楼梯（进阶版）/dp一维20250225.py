m, n=input().split(' ')
m=int(m) # 每次最多可以爬m阶
n=int(n) # 需要爬到楼顶的台阶数

# 1. dp数组以及下标的含义：dp[i]表示爬到第i个台阶的楼顶，有dp[i]种方法
# 2. 递推公式：dp有多种来源，包括dp[i-1], dp[i-2], ..., dp[i-j]
# dp[i]+=dp[i-j]
# 3. 初始化：dp[0]=1
# 如果dp[0]=0的话，那么一切都是0
# 4. 遍历顺序：先遍历背包，后遍历物品

dp=[0]*(n+1)
dp[0]=1

for j in range(1, n+1): # 先遍历背包
    for i in range(1, m+1): # 后遍历物品
        if j>=i: # 确保背包可以容纳物品
            dp[j]+=dp[j-i]

print(dp[n])