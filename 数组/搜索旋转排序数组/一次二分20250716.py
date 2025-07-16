# 由于需要O(logn)的时间复杂度，因此需要使用二分法
# 思路：判断当前mid为分割位置分割出来的两个部分[left, mid]和[mid+1, right]哪个部分是有序的


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            if nums[0]<=nums[mid]:
                if nums[0]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target<=nums[len(nums)-1]:
                    left = mid+1
                else:
                    right = mid-1
        return -1



