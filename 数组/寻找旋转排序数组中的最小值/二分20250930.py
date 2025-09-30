class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[-1]: # mid在第一段中，此时最小值在右侧
                left=mid+1
            else: # mid在第二段中
                right = mid
        return nums[right]