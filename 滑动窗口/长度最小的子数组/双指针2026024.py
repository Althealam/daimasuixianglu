class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        sum_ = 0
        left = 0
        for right in range(len(nums)):
            sum_+=nums[right]
            while sum_>=target:
                min_length = min(min_length, right-left+1)
                sum_-=nums[left]
                left+=1
        return min_length if min_length!=float('inf') else 0