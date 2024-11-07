# 第一种：左闭右开

# 在升序数组nums中寻找目标值target，对于特定下标i，比较nums[i]和target的大小
# 1. 如果nums[i]=target：下标i就是要寻找的下标
# 2. 如果nums[i]>target：target在i的左侧
# 3. 如果nums[i]<target：target在i的右侧

# 时间复杂度：O(logn)，其中n是数组的长度
# 空间复杂度：O(1)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right=0, len(nums)-1
        while left<=right:
            mid=(left+right)//2
            num=nums[mid]
            if num==target:
                return mid
            elif num>target:
                right=mid-1
            else:
                left=mid+1
        return -1