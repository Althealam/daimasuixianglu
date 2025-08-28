# 1. dp数组以及下标的含义：dp[i]表示容量为i的背包，最多可以背的最大重量为dp[i]
# 2. 递推公式
# （1）不背物品i：dp[j]
# （2）背物品i：dp[j-stones[i]]+stones[i]
# dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
# 3. 初始化：最大容量为30*100=3000 由于只需要一般 因此初始化为1500即可
# 4. 遍历顺序：先物品后背包 背包逆序
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = [0]*1501
        total_sum = sum(stones)
        target = total_sum//2

        for stone in stones:
            for j in range(target, stone-1, -1):
                dp[j] = max(dp[j], dp[j-stone]+stone)
        return total_sum-2*dp[target]
        