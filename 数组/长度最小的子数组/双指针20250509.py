# 思路：
# 定义slow和fast，计算slow到fast区间内的元素值sum_
# 1. 如果sum_<target：fast+=1
# 2. 如果sum_>=target：slow+=1
# 更新result=min(result, fast-slow+1)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        sum_=0
        result=float('inf') # 计算符合条件的区间长度
        while right<len(nums):
            sum_+=nums[right]
            while sum_>=target:
                result=min(result, right-left+1)
                sum_-=nums[left]
                left+=1
            right+=1
        return result if result!=float('inf') else 0


        