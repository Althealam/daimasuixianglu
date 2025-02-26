# 1. dp数组以及下标的含义：dp[j]表示凑成金额为j的情况下需要的最少硬币数
# 2. 递推公式：dp[j]=min(dp[j], dp[j-coins[i]]+1)
# （1）不考虑coins[i]：dp[j]
# （2）考虑coins[i]：dp[j-coins[i]]+1
# 3. 初始化：dp[0]=0，其他的初始化为无穷大（因为这里要求解最小值）
# 4. 遍历顺序：先物品后背包，先背包后物品都可以

# 时间复杂度：O(mxn)
# 1. 外层循环：O(n)，n是硬币数组的长度
# 2. 内层循环：O(m)，m是目标金额
# 空间复杂度：O(m)
# 使用了一个长度为amount+1的一维dp数组来保存中间结果

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 最开始需要将dp数组初始化为无穷大，因为本题是求最小值
        dp=[float('inf')]*(amount+1)
        # dp[0]表示凑成金额为0的情况下最少有0个硬币
        dp[0]=0
        for i in range(len(coins)): # 遍历物品
            for j in range(coins[i], amount+1): # 遍历背包
                dp[j]=min(dp[j], dp[j-coins[i]]+1)
        
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]
        