# 1. dp数组以及下标的含义：dp[j]表示凑成总金额为j的货币组合数为dp[j]
# 2. 递推公式：dp[j]+=dp[j-coins[i]]
# 3. 初始化：dp[0]=1 
# 4. 遍历顺序：先物品后背包，背包逆序
# 时间复杂度：O(m*n)，m是硬币数量，n是目标金额
# 空间复杂度：O(n)

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp=[0]*(amount+1)
        dp[0]=1 # 一定要初始化
        for i in range(len(coins)): # 遍历物品
            for j in range(coins[i], amount+1): # 遍历背包
                dp[j]+=dp[j-coins[i]]
        return dp[amount]