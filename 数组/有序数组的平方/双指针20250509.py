# 思路：
# 数组是有序的，那么平方后数组的最大值只会出现在数组的第一个和最后一个位置
# 定义双指针，让left指向0，right指向len(nums)-1
# 每次判断nums[left]*nums[left]和nums[right]*nums[right]的值
# 1. nums[left]*nums[left]<nums[right]*nums[right]: result[k]=nums[right]*nums[right] right-=1
# 2. nums[left]*nums[left]>nums[right]*nums[right]: result[k]=nums[left]*nums[left] left+=1

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        k=len(result)-1
        left=0
        right=len(nums)-1
        while left<=right:
            if nums[left]*nums[left]<nums[right]*nums[right]:
                result[k]=nums[right]*nums[right]
                k-=1
                right-=1
            elif nums[left]*nums[left]>=nums[right]*nums[right]:
                result[k]=nums[left]*nums[left]
                k-=1
                left+=1
        return result

        