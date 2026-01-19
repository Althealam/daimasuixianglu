class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1, -1]
        index = self.binary_search(nums, target)
        if index==-1:
            return [-1, -1]
        left, right = index, index
        while left>0 and nums[left-1]==target:
            left-=1
        while right<len(nums)-1 and nums[right+1]==target:
            right+=1
        return [left, right]
        
    
    def binary_search(self,  nums, target):
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return -1