# 1. dp数组以及下标的含义：dp[j]表示凑成金额为j的硬币组合数为dp[j]
# 2. 递推公式：
# （1）使用coin：dp[j-coin]
# （2）不使用coint：dp[j]
# dp[j]+=dp[j-coin]
# 3. 初始化：dp[0]=1
# 4. 遍历顺序：先物品后背包，完全背包的一维数组遍历背包的时候不需要逆序

amount=int(input())
coins=list(map(int, input().split()))

def ditui(amount, coins):
    dp=[0]*(amount+1)
    dp[0]=1
    for coin in coins: # 遍历物品
        for j in range(coin, amount+1): # 遍历背包
            dp[j]+=dp[j-coin]
    return dp[-1]

result=ditui(amount, coins)
print(result)