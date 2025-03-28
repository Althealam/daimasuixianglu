# 1. dp数组以及下标的含义：满足加法的总和值为i的方法数为dp[i]
# 2. 递推公式：dp[j]+=dp[j-nums[i]]
# 3. 初始化：dp=[0]*(target_sum+1)（target_sum是目标和，也就是left的背包容量）
# 3. 遍历顺序：从左到右

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_=sum(nums)
        # left-right=target
        # left+right=sum_
        # 由此可以知道left=(target+sum_)//2
        # 我们只要找到装满背包容量为(target+sum_)//2的方法数即可

        if abs(target)>sum_: # 目标和大于数组总和，没有方案
            return 0
        if (target+sum_)%2!=0: # 无法凑出left，没有方案
            return 0 

        target_sum=(target+sum_)//2
        dp=[0]*(target_sum+1)
        dp[0]=1
        for num in nums: # 遍历物品
            for j in range(target_sum, num-1, -1): # 逆序遍历背包
                dp[j]+=dp[j-num]
        return dp[target_sum]
        