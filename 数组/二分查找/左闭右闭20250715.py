# 思路：
# 1. 定义left和right，mid=(left+right)//2，判断mid和target的值
# 2. 如果nums[mid]>target则让right=mid；如果nums[mid]<target则让left=mid；如果nums[mid]==target则返回mid
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]<target:
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
            else:
                return mid
        return -1