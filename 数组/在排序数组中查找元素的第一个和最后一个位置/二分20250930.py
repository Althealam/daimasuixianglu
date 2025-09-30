class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ind = self.erfenchazhao(nums, target)
        if ind==-1:
            return [-1, -1]
        else:
            left, right = ind, ind
            while left-1>=0 and nums[left-1]==nums[left]:
                left-=1
            while right+1<=len(nums)-1 and nums[right+1]==nums[right]:
                right+=1
            return [left, right]
        
    def erfenchazhao(self, nums, target):
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
        