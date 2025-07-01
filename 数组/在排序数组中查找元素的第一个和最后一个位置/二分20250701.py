# 思路：通过二分查找找到第一个等于target的元素下标
# 1. 没找到：直接返回[-1,-1]
# 2. 找到了：左右移动指针，找到满足题目含义的区间
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = self.erfenchazhao(nums, target)
        if ans == -1:
            return [-1, -1]
        else:
            left, right = ans, ans 
            # 向左移动指针
            while left>=0 and nums[left-1]==target:
                left -=1
            # 向右移动指针
            while right<=len(nums)-1 and nums[right+1]==target:
                right+=1
        return [left, right]
    
    def erfenchazhao(self, nums, target):
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>target: # target在[left, mid-1]中
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
            else:
                return mid
        return -1
            
        