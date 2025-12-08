class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0 # the longest distance you can reach so far
        current_distance = 0
        for i in range(len(nums)):
            if i>cover: # you can not achieve this space, so we can return False directly
                return False
            if cover>=len(nums)-1: # you can cover the last index
                return True
            current_distance = nums[i]+i
            cover = max(cover, current_distance)
        return False