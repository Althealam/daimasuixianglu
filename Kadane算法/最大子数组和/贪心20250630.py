# 贪心法：每次都加上nums[i]，判断当前count是否大于0，如果大于0的话则和已知的最大子数组和比较，如果超过的话则更新，没有超过的话则count=0，继续遍历
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        count = 0
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            count+=nums[i]
            result = max(result, count)
            if count<0:
                count=0
        return result

