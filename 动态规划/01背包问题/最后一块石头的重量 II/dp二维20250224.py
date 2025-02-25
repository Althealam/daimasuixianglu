# 思路：将这堆石头分成两堆，假设这两堆石头的重量分别是sum1和sum2，并且sum1>=sum2，那么最后剩下的石头重量就是sum1-sum2。
# 我们的目标是要让这个差值尽可能的小，也就是sum1和sum2尽可能的接近，并且sum=sum1+sum2是固定的，因此sum2尽可能的接近sum/2的时候，sum1-sum2就会最小

# 1. dp数组以及下标的含义：dp[i][j]表示前面i个是否能组成重量j
# 2. 递推公式：
# （1）当前石头重量大于当前重量j：dp[i][j]=dp[i-1][j]
# （2）当前石头重量小于等于当前重量：dp[i][j]=dp[i-1][j] or dp[i-1][j-stones[i-1]]
# 3. 遍历方向：从左到右
# 4. 初始化：重量：target+1 物品数：len(stones)+1 物品数行，重量列

# 时间复杂度：O(nxtarget)
# 空间复杂度：O(nxtarget)

# stones=list(map(int, input().split())) ACM模式
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        total_sum=sum(stones)
        target=total_sum//2

        dp=[[False]*(target+1) for _ in range(len(stones)+1)]

        # 初始化第一列，当背包容量为0的时候，都为True
        for i in range(len(stones)+1):
            dp[i][0]=True

        for i in range(1, len(stones)+1): # 遍历物品
            for j in range(1, target+1): # 遍历背包
                # 如果当前石头重量大于当前目标重量，则无法选择该石头
                if stones[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                # 可以选择是否也可以不选择是否
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-stones[i-1]]
        
        # 找到最大的重量i，使得dp[len(stones)][i]为True
        # 返回总重量减去两倍的最接近总重量一半的重量
        for i in range(target, -1, -1):
            if dp[len(stones)][i]:
                return total_sum-2*i
        
        return True
