# 方法二：暴力排序法+列表推导法
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return sorted(x*x for x in nums)