class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            # 判断一下mid在哪个位置
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]: # mid和left在同一段
                if nums[left]<=target<=nums[mid]: # mid, target, left在同一段，并且target在两者中间
                    right=mid-1
                else: # target在mid的右边
                    left=mid+1
            else: # mid和left不在同一段
                if nums[mid]<=target<=nums[right]: # mid, target, right在同一段，并且target在两者的中间
                    left=mid+1
                else: # target在mid的左边
                    right=mid-1
        return -1