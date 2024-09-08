# 方法一：暴力排序法
# 利用sort()进行排序
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index=0
        for i in range(len(nums)):
            nums[index]=nums[i]*nums[i]
            index+=1
        nums.sort()
        return nums