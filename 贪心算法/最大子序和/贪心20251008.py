class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        sum_ = 0
        for i in range(len(nums)):
            sum_+=nums[i]
            if sum_>res:
                res = sum_
            if sum_<0:
                sum_=0
        return res