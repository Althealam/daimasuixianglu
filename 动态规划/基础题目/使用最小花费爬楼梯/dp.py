# Eg：cost = [10,15,20]
# 注意：1. 顶楼指的是下标为3的位置 2. 只有当你向上爬的时候，才会产生花费
# 分析：判断dp[i]的花费
# 1. 由dp[i-1]往上爬一步：dp[i-1]+cost[i-1]
# 2. 由dp[i-2]往上爬两步：dp[i-2]+cost[i-2]
# 由于我们求的是最小花费，因此min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
# 动态规划五部曲
# 1. dp[i]：到达下标i的花费为dp[i]
# 2. 递归公式：dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
# 3. 初始化：dp[0]=0 dp[1]=0 （只有向上爬的时候才会产生花费）
# 4. 遍历顺序：从前往后遍历

# 时间复杂度：O(n)
# 1. 初始化dp数组：O(n)
# 2. 动态规划填充dp数组：O(n)
# 空间复杂度：O(n)
# 1. dp数组：O(n)
# 2. 常数空间
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp=[0]*(len(cost)+1)
        dp[0],dp[1]=0,0
        for i in range(2,len(cost)+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
        
        return dp[len(cost)]

        