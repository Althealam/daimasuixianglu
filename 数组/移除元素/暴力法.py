# 方法一：暴力法
# 两个循环，一个循环遍历数组，一个循环更新数组
# 返回移除后数组的新长度
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n=len(nums)
        i=0
        while i<n:
            if nums[i]==val:
                for j in range(i+1,n):
                    nums[j-1]=nums[j]
                n-=1
                i-=1
            i+=1
        return n