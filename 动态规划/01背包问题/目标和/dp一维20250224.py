# 分析：假设加法的总和是x，那么减法的总和就是sum(nums)-x
# 我们需要x-(sum(nums)-x)==target： x=(target+sum)/2 找到是否满足x的值为(target+sum)/2的目标数 背包容量为(target+sum)/2

# 1. dp数组的下标及其含义：dp[i]表示如果要满足加法的总和值为x的方法数为dp[i]
# 2. 递推公式：dp[j]+=dp[j-num]
# 3. 初始化：dp=[0]*(target_sum+1)，其中target_sum就是(target+sum)/2，也就是背包容量
# dp[0]=1
# 4. 遍历顺序：从左到右

# 时间复杂度：O(nxtarget_sum)
# 空间复杂度：O(target_sum)

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_sum=sum(nums)
        # 目标和的数量已经超过了总和，没有方案
        if abs(target)>total_sum:
            return 0 
        # 没法凑到加法的目标和
        if (target+total_sum)%2!=0:
            return 0
        target_sum=(target+total_sum)/2
        dp=[0]*(1+target_sum) # 初始化dp数组
        dp[0]=1 # 目标和为0的时候，只有一种方法，就是什么都不选
        for num in nums: # 遍历物品
            for j in range(target_sum, num-1, -1): # 遍历背包
                dp[j]+=dp[j-num] # 状态转移方程，累加不同选择方式的数量
        return dp[target_sum] # 返回达到目标和的方案数



