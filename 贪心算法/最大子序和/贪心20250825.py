class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ans = float('-inf') # 最大子序列和
        current_ans = 0 # 当前的子数组和
        for i in range(len(nums)):
            current_ans+=nums[i]
            if current_ans>max_ans:
                max_ans = current_ans
            if current_ans<0:
                current_ans = 0
        return max_ans
            