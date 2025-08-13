# 思路：定义单调栈，栈中存储还没遇到右边第一个大于它的值的元素
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        stack = []
        for i in range(len(nums)):
            while stack and nums[i]>=nums[stack[-1]]:
                stack.pop()
            stack.append(i)
        return stack[0]
        