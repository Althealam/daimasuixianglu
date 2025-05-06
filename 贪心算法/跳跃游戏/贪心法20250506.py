# 思路：
# 1. 遍历nums
# 2. 判断目前的i是否在cover范围内
# 3. 如果是的话，更新cover=max(i+nums[i], cover)，判断cover是否达到了len(nums)-1，如果超过了则返回True，否则返回False
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover=0
        for i in range(len(nums)):
            if i<=cover:
                cover=max(i+nums[i], cover)
        if cover>=len(nums)-1:
            return True
        return False

