# 1. dp数组的下标及含义：dp[i]表示爬到第i个台阶时需要花费的最小花费
# 2. 递推公式：
# （1）从i-2开始向上爬：dp[i-2]+cost[i-2]
# （2）从i-1来时向上爬：dp[i-1]+cost[i-1]
# 3. 遍历顺序：从左到右遍历
# 4. dp数组初始化：dp[0]=0 dp[1]=0 （因为可以从下标为0或者下标为1的台阶开始爬楼梯）
# 注意：到达楼梯顶部指的不是到达数组的最后一个元素，而是到达数组的末尾，也就是数组的最后一个元素的后面

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp=[0]*(len(cost)+1)
        dp[0]=0
        dp[1]=0
        for i in range(2,len(cost)+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        return dp[len(cost)]

        