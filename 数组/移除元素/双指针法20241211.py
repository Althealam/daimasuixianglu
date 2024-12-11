# 双指针法
# 1. 定义一个slow和fast，slow用来遍历数组nums，指向更新新数组的下标，fast用来遍历数组nums中不等于val的元素（新数组的元素）
# 2. 如果nums[fast]==val: fast+=1
#    如果nums[fast]!=val: nums[slow]=nums[fast] slow+=1 fast+=1
# 不管nums[fast]是否等于val，都需要将fast+=1

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow, fast=0, 0
        while fast<=len(nums)-1:
            if nums[fast]==val:
                fast+=1
            else:
                nums[slow]=nums[fast]
                slow+=1
                fast+=1
        return slow
            
        