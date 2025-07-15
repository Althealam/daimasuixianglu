# 思路：定义left和right，计算left到right区间内的元素值sum_

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        sum_ = 0 # 区间和
        ans = float('inf')
        while right<len(nums):
            sum_+=nums[right]
            while sum_>=target:
                ans = min(ans, right-left+1)
                sum_-=nums[left]
                left+=1
            right+=1
        return ans if ans!=float('inf') else 0
