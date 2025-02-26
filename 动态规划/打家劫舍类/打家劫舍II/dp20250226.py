# 分析：成环主要有三种情况：
# （1）考虑不包含首尾元素
# （2）考虑包含首元素，不包含尾元素（考虑，但是不一定要真的有）
# （3）考虑包含尾元素，不包含首元素（考虑，但是不一定要真的有）
# 前面的第二种情况和第三种情况包含了第一种情况
# 1. dp数组以及下标的含义：dp[i]表示考虑下标i以内的房屋，最多可以偷窃的金额为dp[i]
# 2. 递推公式：dp[i]=dp[i-1]+dp[i-2]
# 3. 遍历顺序：从前向后便利
# 4. 初始化：dp[0]=nums[0] dp[1]=max(nums[0], nums[1])

# 时间复杂度：
# 1. rob函数：边界条件的判断为O(1)
# 2. robRange函数：for循环填充dp数组，循环从start+2到end+1，循环次数为end-start，循环的次数最多是O(n)
# 3. 总体时间复杂度：O(n)

# 空间复杂度：O(n)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0: # 没有房屋的情况下直接返回
            return 0
        if len(nums)==1: # 如果只有一个房屋则直接返回第一个房屋可以偷的钱
            return nums[0]
        dp=[0]*len(nums)
        result1=self.robRange(nums, 0, len(nums)-2, dp) # 考虑首元素，不考虑尾元素
        result2=self.robRange(nums, 1, len(nums)-1, dp) # 考虑尾元素，不考虑首元素

        return max(result1, result2)
    
    def robRange(self, nums, start, end, dp):
        # 和打家劫舍的代码逻辑一模一样，不一样的是start和end
        if end==start:
            return nums[start]
        dp[start]=nums[start]
        dp[start+1]=max(nums[start], nums[start+1])
        for i in range(start+2, end+1):
            dp[i]=max(dp[i-1], dp[i-2]+nums[i])
        return dp[end]


        
        
        