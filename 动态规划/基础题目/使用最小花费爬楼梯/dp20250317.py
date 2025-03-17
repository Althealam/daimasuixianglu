# 1. dp数组以及下标的含义：dp[i]表示爬到第i个台阶需要支付的最小的费用
# 2. 递推公式：
# （1）从下一个台阶爬上来：dp[i-1]+cost[i-1]
# （2）从下两个台阶爬上来：dp[i-2]+cost[i-2]
# 3. 初始化：dp[0]=0 dp[1]=0
# 4. 遍历顺序：从左到右
# 5. 注意，一定是达到len(cost)，因为需要跳过最后一个台阶才能到达楼顶

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)+1)
        dp[0]=0
        dp[1]=0
        if len(cost)==1:
            return dp[1]
        for i in range(2, len(cost)+1):
            dp[i]=min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        return dp[len(cost)]


    
        