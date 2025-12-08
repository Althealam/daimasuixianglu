class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0 # the minimum number of jumps to reach index n-1
        current_end = 0 # current longest distance
        next_end = 0 # next longest distance
        for i in range(len(nums)-1):
            next_end = max(next_end, nums[i]+i)
            if i==current_end:
                ans+=1
                current_end = next_end
        return ans
            