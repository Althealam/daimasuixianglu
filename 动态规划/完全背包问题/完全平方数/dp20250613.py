# 1. dp数组以及下标的含义：dp[j]表示和为j的完全平方数的最少数量为dp[j]
# 2. 递推公式：
# （1）不使用i：dp[j]
# （2）使用i：dp[j-i**2]+1
# dp[j]=min(dp[j], dp[j-i**2]+1)
# 3. 初始化：dp[0]=0 全部初始化为正无穷
# 4. 遍历顺序：先物品后背包，本题是完全背包并且是求组合数

n = int(input())

def ditui(n):
    dp=[float('inf')]*(n+1)
    dp[0]=0

    for i in range(1, n+1): # 遍历物品
        for j in range(i**2, n+1): # 遍历背包
            dp[j]=min(dp[j], dp[j-i**2]+1)
    return dp[-1] 

result=ditui(n)
print(result)