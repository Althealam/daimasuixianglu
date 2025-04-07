# 1. dp数组以及下标的含义：dp[i]表示偷窃[0,i]的房屋时可以偷窃到的最大金额为dp[i]
# 2. 递推公式：dp[i]=max(dp[i-1], dp[i-2]+nums[i])
# （1）考虑不包含首尾元素：由于1情况已经被2和3情况包含了，因此不做考虑
# （2）考虑首元素，不考虑尾元素
# （3）考虑尾元素，不考虑首元素
# 3. 初始化和打家劫舍相同：dp[0]=nums[0] dp[1]=max(nums[0], nums[1])
# 4. 遍历顺序：从前向后遍历

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        # 1. 考虑首元素，不考虑尾元素
        start=0
        end=len(nums)-2
        result1=self.robrange(nums[start:end+1])
        # 2. 考虑尾元素，不考虑首元素
        start=1
        end=len(nums)-1
        result2=self.robrange(nums[start:end+1])
        return max(result1, result2)
    
    def robrange(self, nums):
        """
        根据已给的nums求解能够偷窃到的最大金额
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i]=max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]
        