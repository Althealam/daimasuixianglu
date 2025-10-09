class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        for i in range(len(nums)):
            if i>cover:
                return False
            cover = max(cover, i+nums[i])
            if cover>=len(nums)-1:
                return True
        return False