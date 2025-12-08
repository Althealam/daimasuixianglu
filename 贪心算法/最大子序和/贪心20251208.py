class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_=0
        max_sum = float('-inf')
        for i in range(len(nums)):
            sum_+=nums[i]
            if sum_>max_sum:
                max_sum = max(max_sum, sum_)
            if sum_<0:
                sum_=0
        return max_sum if max_sum!=float('-inf') else 0
                