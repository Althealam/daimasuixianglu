# 思路：
# 1. 定义left和right，mid=(left+right)//2，判断mid和target的值
# 2. 如果nums[mid]>target则让right=mid；如果nums[mid]<target则让left=mid；如果nums[mid]==target则返回mid
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target: # 说明target在[mid+1, right]这个区间内
                left=mid+1
            elif nums[mid]>target: # 说明target在[left, mid-1]这个区间内
                right=mid-1
            else:
                return mid
        return -1

        