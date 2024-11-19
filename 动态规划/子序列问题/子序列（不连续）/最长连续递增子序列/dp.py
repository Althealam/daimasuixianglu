# 动态规划五部曲
# 1. dp数组：dp[i]指的是以下标i为结尾的连续递增的子序列的长度
# 2. 递推公式：
# nums[i]>nums[i-1]，那么dp[i]=dp[i-1]+1
# 3. 初始化：dp[i]=1
# 4. 遍历顺序：从前到后

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[1]*len(nums)
        result=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dp[i]=dp[i-1]+1
                result=max(result,dp[i])
        return result


        