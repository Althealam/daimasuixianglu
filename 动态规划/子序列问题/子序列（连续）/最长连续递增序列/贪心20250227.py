# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        result=1 # 连续子序列最少是1
        count=1  # 记录最长连续子序列的值，统计目前统计到的递增子序列长度
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                count+=1
            else:
                count=1
            result=max(result, count)
        return result
            
        