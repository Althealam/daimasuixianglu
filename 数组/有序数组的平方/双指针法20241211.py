# 双指针法
# 思路：数组的平方的最大值只会出现在最左边和最右边（因为这个数组是非递减顺序的）
# 由此可以知道，可以定义一个双指针，每次都计算左右指针的数组的平方值，然后存储到数组里即可

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right=0, len(nums)-1
        i=len(nums)-1
        result=[float('inf')]*len(nums) # 定义结果集，存放有序数组的平方（递减数组）
        while left<=right:
            if nums[left]**2>=nums[right]**2:
                result[i]=nums[left]**2
                left+=1 # 左指针向右移动
            elif nums[left]**2<nums[right]**2:
                result[i]=nums[right]**2
                right-=1 # 右指针向左移动
            i-=1 # 存放结果的指针
        return result
                        

        