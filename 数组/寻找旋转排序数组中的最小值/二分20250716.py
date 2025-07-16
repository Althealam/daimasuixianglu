# 分析：本题的最后一个数字（nums[-1]）要不然是最小值，要不然在最小值的右侧
# 在0到n-2中进行二分
# 1. nums[mid]>nums[-1]
# nums一定被分为了两个递增段；第一段的元素全部大于第二段的元素；nums[mid]在第一段；最小值在第二段；nums[mid]在最小值的左边
# 2. nums[mid]<nums[-1]: nums[mid]可能在第二段，也有可能nums只有一段
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left<right: # 左闭右开，最后最小值在right
            mid = (left+right)//2
            if nums[mid]>nums[-1]: # 数组被分为了两段，因此最小值在第二段，left=mid+1
                left=mid+1
            else: # nums[mid]可能在第二段，也有可能nums只有一段，此时最小值在mid的右边
                right=mid
        return nums[right]
            

