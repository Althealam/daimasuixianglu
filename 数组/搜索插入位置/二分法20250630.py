class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) # 左闭右开区间
        while left<right:
            mid = (left+right-1)//2
            if nums[mid]<target: # target所在区间为(mid+1, right)
                left = mid+1
            elif nums[mid]>target: # target所在区间为(left, mid)
                right = mid
            else: # 找到了target值
                return mid
        return right
        