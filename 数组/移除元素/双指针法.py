# 方法二：双指针法
# 快指针：寻找新数组的元素，新数组就是不含val的数组
# 慢指针：指向更新新数组下标的位置
# 返回移除后数组的新长度
# 备注：不可以使用额外的数组空间，必须仅使用O(1)额外空间并且原地修改输入数组

# 分析：
# fast和slow都从0开始
# 如果nums[slow]==val: fast+=1并nums[slow]=nums[fast]
# 如果nums[slow]!=val: nums[slow]=nums[fast]
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        fast=0 # 快指针
        slow=0 # 慢指针
        size=len(nums)
        while fast<size: # 不加等于是因为fast=size时，数组会越界
            if nums[fast]!=val:
                # slow 用来收集不等于 val 的值，如果 fast 对应值不等于 val，则把它与 slow 替换
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow