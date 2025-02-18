# 思路：覆盖范围思想，判断数组的覆盖范围是否有涵盖数组的最后一个元素
# 计算最远可以到达的覆盖范围：
# 1. 遍历nums
# 2. 判断目前的i是否在覆盖范围内
# 3. 如果是的话，更新最远可覆盖范围：cover=max(i+nums[i],cover)，并且判断最远覆盖范围是否超过了len(nums)-1

# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cover=0 # 表示最远到达的覆盖范围
        if len(nums)==1:
            return True
        for i in range(len(nums)):
            if i<=cover:
                cover=max(i+nums[i],cover)
                if cover>=len(nums)-1:
                    return True
        return False