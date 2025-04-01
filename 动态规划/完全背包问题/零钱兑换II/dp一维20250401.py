# 1. dp数组以及下标的含义：表示凑出背包容量为j有dp[j]种方法
# 2. 递推公式：
# dp[j]+=dp[j-coins[i]]
# 3. 初始化：全部初始化为0 dp[0]=1 表示凑出背包容量为0有1种方法（就是什么都不放）
# 4. 遍历顺序：先物品，后背包
# 注意：本题是组合数，因此是先物品后背包，并且背包不需要逆序
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for coin in coins: # 遍历物品
            for j in range(coin, amount+1):
                dp[j]+=dp[j-coin]
        return dp[amount]
        