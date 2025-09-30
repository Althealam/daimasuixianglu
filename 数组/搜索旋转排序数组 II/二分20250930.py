# 1. 找到数组中的最小值
# 2. 判断target和nums[mid]的大小，来判断target的位置
# （1）target=nums[mid]: 直接return true
# （2）target>nums[mid]: target在第二段数组中，也就是[mid+1, right]
# （3）target<nums[mid]: target在第一段数组中，也就是[left, mid-1]

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        min_index = self.find_min(nums)
        n = len(nums)
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            real_mid = (mid+min_index)%n

            if nums[real_mid]==target:
                return True
            
            elif nums[real_mid]<target: # target在第二段数组中，也就是[mid+1, right]
                left = mid+1
            else: # target在第一段数组中，也就是[left, mid-1]
                right = mid-1
        return False
    
    def find_min(self, nums):
        """寻找旋转点"""
        left, right = 0, len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[right]:
                left = mid+1
            elif nums[mid]<nums[right]:
                right = mid
            else:
                if nums[right-1]>nums[right]:
                    return right
                right-=1
        return left
    
        