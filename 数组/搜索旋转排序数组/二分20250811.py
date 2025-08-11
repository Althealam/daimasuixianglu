# 思路：
# 二分法，首先找到中间元素，判断[left, mid-1]和[mid+1, right]哪边是有序的
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            # 左半段是有序的
            if nums[left]<=nums[mid]: 
                # target在左半段
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                # target在右半段
                else:
                    left=mid+1
            # 右半段是有序的
            else:
                # target在右半段
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                # target在左半段
                else:
                    right=mid-1
        return -1
            

        