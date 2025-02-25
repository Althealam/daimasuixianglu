# 只要能找到一个子集，其和为sum(nums)//2，那么剩下的元素的和也一定是sum(nums)//2
# 1. dp数组以及下标的含义：dp[i][j]表示使用nums的前i个元素，是否能够组合出和为j的子集
# （1）i=0：表示不用数组中的任何一个元素
# （2）i=1：表示只使用数组中的第一个元素
# （3）j=0：表示目标和为0
# （4）j=target_sum：表示目标和为target_sum
# 2. 递推公式
# （1）j<nums[i-1]：dp[i][j]=dp[i-1][j]
# （2）j>=nums[i-1]：dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
# 3. 初始化：dp[i][0]=True
# 4. 遍历顺序：外层循环遍历物品，内层循环遍历背包
# 外层循环的i从1到len(nums)  内层循环的j从1到target_sum

# 时间复杂度：O(n*target_sum)
# 空间复杂度：O(n*target_sum)

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums)%2!=0:
            return False
        
        target_sum=sum(nums)//2 # 目标和

        dp=[[False]*(target_sum+1) for _ in range(len(nums)+1)]

        # 初始化
        # 1. 当背包容量为0的时候，始终为True
        # 2. 当物品容量为0的时候，始终为False
        for i in range(len(nums)+1):
            dp[i][0]=True
        
        # 动态规划
        for i in range(1, len(nums)+1): # 遍历物品
            for j in range(1, target_sum+1): # 遍历背包
                # 当前数字大于目标和的时候，无法使用该数字
                if nums[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                # 当前目标和j大于等于当前元素nums[i-1]时
                else:
                    # 1. 不使用该元素dp[i-1][j]
                    # 2. 使用该元素dp[i-1][j-nums[i-1]]
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
        
        return dp[len(nums)][target_sum]
            