# dp（先物品后背包）
# 完全背包问题，求能够凑成总金额所需要的最少的硬币组合数
# 1. dp数组的含义：dp[j]表示凑到总金额为j时所需要的最少的硬币组合数
# 2. 递推公式：凑足金额j-coins[i]的最少个数为dp[j-coins[i]]，那么只需要加上一个钱币coins[i]就是dp[j]
# 也就是说dp[j]=dp[j-coins[i]]+1
# dp[j]=min(dp[j],dp[j-coins[i]]+1)
# 3. 初始化：
# （1）dp[0]=0（凑足总金额为0所需要的钱币个数为0）
# （2）dp[j]必须要初始化为一个最大的数，否则就会在min(dp[j-coins[i]]+1,dp[j])中被覆盖掉
# 4. 遍历顺序：先物品，后背包
# （1）求组合数：外层for循环遍历物品，内层for循环遍历背包
# （2）求排列数：外层for循环遍历背包，内层for循环遍历物品

# 时间复杂度：
# 1. 外层循环coins，假设硬币的数量为n
# 2. 内层循环：amount-coin+1
# 总的时间复杂度为O(nxamount)
# 空间复杂度：
# 1. 需要一个大小为amount+1的dp数组来存储
# 总的空间复杂度为O(amount)

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[float('inf')]*(amount+1) # 创建动态规划数组，初始值为正无穷大
        dp[0]=0 # 初始化背包容量为0时的最小硬币数量为0
        for coin in coins: # 遍历硬币列表
            for j in range(coin,amount+1): # 遍历背包容量
                if dp[j-coin]!=float('inf'): # 如果dp[i-coin]不是初始值，则进行状态转移
                    dp[j]=min(dp[j-coin]+1,dp[j]) # 更新最小硬币数量
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]