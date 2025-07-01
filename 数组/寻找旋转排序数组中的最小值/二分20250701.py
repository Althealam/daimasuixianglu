# 分析：本题的最后一个数字（nums[-1]）要不然是最小值，要不然在最小值的右侧
# 在0到n-2中进行二分
# 1. nums[mid]>nums[-1]
# nums一定被分为了两个递增段；第一段的元素全部大于第二段的元素；nums[mid]在第一段；最小值在第二段；nums[mid]在最小值的左边
# 2. nums[mid]<nums[-1]: nums[mid]可能在第二段，也有可能nums只有一段
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left<right: # 终止条件是left==right
            mid = (left+right)//2
            if nums[mid]<nums[-1]: # nums[-1]在第二段，或者此时只有一段（最小值在mid的左侧，包含mid）
                right = mid
            else: # nums被分为了两段，nums[mid]在最小值的左边（最小值在mid的右侧，不包含mid）
                left = mid+1
        return nums[right]