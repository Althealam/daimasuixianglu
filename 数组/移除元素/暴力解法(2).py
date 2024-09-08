# 方法三：暴力解法（二）
# 使用index找到不等于val的所有数组元素

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index=0
        # nums[index]相当于一个新数组（去掉了val后的数组）
        # 利用if nums[i!=val查找nums中所有不等于val的数组元素
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[index]=nums[i]
                index+=1
        return index

