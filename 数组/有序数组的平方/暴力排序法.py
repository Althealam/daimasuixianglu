# 方法一：暴力排序法
# 利用sort()进行排序
# 时间复杂度：
# 1. 遍历数组求平方：O(n)
# 2. sort：排序操作的时间复杂度为O(nlogn)
# 总的时间复杂度：O(n)+O(nlogn)=O(nlogn)
# 空间复杂度：
# 1. 平方操作：在原数组中进行的，因此为O(1)
# 2. 排序操作：sort()是在原地排序的，总体复杂度为O(1)
# 总的空间复杂度：O(1)
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        return nums