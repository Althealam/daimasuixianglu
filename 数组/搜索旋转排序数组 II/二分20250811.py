# 思路：
# 1. 找到数组的最小值
# 2. 判断nums[mid]和target的大小，判断target的位置
# （1）target==nums[mid]，直接return True
# （2）target>nums[mid]：target在第一段数组中，也就是[mid+1, right]
# （3）target<nums[mid]：target在第二段数组中，也就是[left, mid-1]
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        min_index = self.find_min(nums) # 最小值用于寻找数组的断点

        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            real_mid = (mid+min_index)%len(nums) # 计算实际索引（将其拉直回原本的有序数组）==> 最小值索引为min_index，相当于将有序数组旋转了min_index位

            if nums[real_mid]==target: 
                return True
            elif nums[real_mid]<target: # target在第二段数组中
                left = mid+1
            else:
                right = mid-1
        return False
    
    def find_min(self, nums):
        """在有重复元素的旋转数组中寻找最小值"""
        left, right = 0, len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[right]: # mid在第一段数组中，因此最小值在[mid+1, right]中
                left = mid+1
            elif nums[mid]<nums[right]: # mid在第二段数组中，因此最小值在[left, mid]中
                right = mid
            else:
                if nums[right-1]==nums[right]:
                    return right # 找到旋转点
                right-=1
        return left