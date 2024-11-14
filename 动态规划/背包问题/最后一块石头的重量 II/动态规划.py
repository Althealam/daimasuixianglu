# 分析：尽可能的分成两堆，让重量相近的放在一起。每个物品只能用一次，因此这道题也是0-1背包问题。
# 本题物品的重量为stones[i]，物品的价值也是stones[i]（对应着01背包里的物品重量weight[i]和物品价值value[i]）

# 核心思想：如何选择石头，使得最终剩下的石头重量尽可能小，甚至为0

# 动态规划五部曲：
# 1. dp数组：dp[j]背包容量为j时背包的最大价值为dp[j]
# 2. 递推公式：dp[j]=max(dp[j],dp[j-weight[i]]+value[i]) 本题中的weight就是我们的value
# 也就是：dp[j]=max(dp[j],dp[j-stone[i]]+stone[i])
# 3. 初始化：dp[0]=0
# 由于1<=stones.length<=30并且1<=stones[i]<=100
# 因此最大重量就是30*100=3000，而我们要求的target其实只是最大重量的一半，因此取1500即可
# 4. 遍历顺序：第一层for循环遍历物品，第二层for循环遍历背包，并且遍历背包时从大到小遍历（如果从小到大遍历，就不是0-1背包了）
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        dp=[0]*15001
        total_sum=sum(stones)
        target=total_sum//2

        for stone in stones: # 遍历物品
            for j in range(target,stone-1,-1): # 遍历背包
                dp[j]=max(dp[j],dp[j-stone]+stone)
        return total_sum-dp[target]-dp[target]
        