class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 左闭右闭区间
        left=0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>target:
                right = mid-1  # target在[left, mid-1]中
            elif nums[mid]<target: 
                left = mid+1 # target在[mid+1, right]中
            else:
                return mid # 找到了target值
        return left # target的插入位置