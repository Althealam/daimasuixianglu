# 思路：将这堆石头分成两堆，假设这两堆石头的重量分别是sum1和sum2，并且sum1>=sum2，那么最后剩下的石头重量就是sum1-sum2。
# 我们的目标是要让这个差值尽可能的小，也就是sum1和sum2尽可能的接近，并且sum=sum1+sum2是固定的，因此sum2尽可能的接近sum/2的时候，sum1-sum2就会最小

# 1. dp数组以及下标的含义：dp[i]表示容量为i的背包，最多可以背的最大重量为dp[i]。本题中石头的重量是stones[i]，石头的价值就是stones[i]
# 2. 递推公式：dp[i]=max(dp[i], dp[i-weight[j]]+value[j])
# 也就是：dp[i]=max(dp[i],dp[i-stones[j]]+stones[j])
# 3. dp数组的初始化：由题可以知道1<=stones.length<=30, 1<=stones[i]<=1000，因此最大重量是30*1000=30000
# 我们要求的target是最大重量的一半，因此将dp数组开到15000即可
# 4. 确定遍历顺序：一维dp数组，物品遍历放在外面，背包遍历放在里面，并且内层for循环倒序遍历

# 时间复杂度：O(n*target)，n是石头的数量，target是所有石头总重量的一半
# 空间复杂度：O(1)，用来存储dp数组

# stones=list(map(int, input().split())) ACM模式
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total_sum=sum(stones)
        target=total_sum//2 # 计算目标和

        dp=[0]*15001 # 初始化dp数组 

        for stone in stones: # 遍历物品
            for j in range(target, stone-1, -1): # 遍历背包
                dp[j]=max(dp[j],dp[j-stone]+stone)
        return total_sum-dp[target]-dp[target]
        # dp[target]指的是不超过目标重量target的情况下，能选择的石头的最大重量
        # 我们将石头分成了两堆，一堆是dp[target]，另外一堆就是total_sum-dp[target]




        