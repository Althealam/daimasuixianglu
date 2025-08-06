# 思路：通过二分查找找到其位置，然后定义left和right去找到其左右边界
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ind = self.erfenchazhao(nums, target)
        if ind==-1:
            return [-1, -1]
        else:
            left, right = ind, ind
            while left-1>=0 and nums[left-1]==target:
                left-=1
            while right+1<=len(nums)-1 and nums[right+1]==target:
                    right+=1
            return [left, right]
        
    def erfenchazhao(self, nums, target):
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]<target: # target在右边
                left = mid+1
            elif nums[mid]>target:
                right = mid-1
            else:
                return mid
        return -1
        