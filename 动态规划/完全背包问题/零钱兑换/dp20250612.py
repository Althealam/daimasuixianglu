# 1. dp数组以及下标的含义：dp[j]表示凑成金额j时所需要的最少的硬币个数为dp[j]
# 2. 递推公式：
# （1）使用coin：dp[j-coin]+1
# （2）不使用coin：dp[j]
# dp[j]=min(dp[j], dp[j-coin]+1)
# 3. 初始化：全部初始化为正无穷 dp[0]=0
# 4. 遍历顺序：本题求组合数，先物品后背包背包逆序
coins=list(map(int, input().split()))
amount=int(input())


def ditui(coins, amount):
    dp=[float('inf')]*(amount+1)
    dp[0]=0
    for coin in coins: # 遍历物品
        for j in range(coin, amount+1): # 遍历背包
            dp[j]=min(dp[j], dp[j-coin]+1)
    if dp[-1]==float('inf'):
        return -1
    return dp[-1]

result=ditui(coins, amount)
print(result)

