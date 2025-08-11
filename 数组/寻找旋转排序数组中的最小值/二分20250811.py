# 旋转数组的特性：
# 1. 旋转后的数组可以分为两个递增子段
# 2. 第二段的所有元素都小于第一段，并且最小值一定是第二段的第一个元素
# 3. nums[-1]要么是最小值，要么比最小值大

# 本题的nums[-1]要不然就是最小值，要不然就是比最小值大
# （1）nums[mid]>nums[-1]：nums被分为了两个递增段，并且第一段的元素全部大于第二段的元素，mid在第一段中
# （2）nums[mid]<nums[-1]：nums[mid]可能在第二段，也可能nums只有一段

# 在[0, len(nums)-2]中查找最小值
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[-1]: # mid在第一段中，此时最小值在右侧，也就是left=mid+1
                left = mid+1
            else: # mid在第二段中，最小值可能是mid也可能在其左侧，因此right=mid
                right = mid
        return nums[right]

        