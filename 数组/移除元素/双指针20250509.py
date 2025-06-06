# 思路：
# 定义快慢指针，快指针的作用是指向元素值不为val的元素，遇到后则进行覆盖，当快指针达到最后一个元素时则结束
# 1. 快指针：寻找新数组的元素，新数组就是不含有目标元素的数组
# 2. 慢指针：指向更新新数组下标的位置

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow=0
        fast=0
        while fast<len(nums): # 如果fast达到len(nums)，那么nums会越界
            if nums[fast]!=val:
                nums[slow]=nums[fast]
                slow+=1 # 说明此时已经填充了新数组的一个下标，需要到下一个下标去
            fast+=1
        return slow