# 思路：
# 1. 先将nums排序
# 2. 选择nums中小于0的元素进行取反，同时k-=1，直到k=0
# 3. 如果最后k=0，则结束；如果最后k>0，则找最小的元素进行取反
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        # 先找到小于0的元素进行取反操作
        for i in range(len(nums)):
            if nums[i]<0 and k>0:
                nums[i]=-1*nums[i]
                k-=1
        # 其次，当k>0时，则继续处理元素
        nums.sort()
        while k>0:
            nums[0]=-1*nums[0]
            k-=1
        return sum(nums)
        