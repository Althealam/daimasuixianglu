# 思路：
# 1. 遍历数组nums，获取当前位置可以跳跃到达的最大位置max_cover = max(max_cover, i+nums[i])
# 2. 每次跳跃的时候都判断i是否在max_cover内，不在的话则直接返回False
# 3. 如果max_cover>=len(nums)-1，则直接返回True
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
        