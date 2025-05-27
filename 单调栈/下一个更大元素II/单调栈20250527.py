# 思路：
# 1. 定义单调栈，存储nums中还没找到答案的元素值的下标
# 2. 遍历2*len(nums)，如果当前遍历的元素值大于栈顶元素，则栈顶元素找到了答案值，弹出栈顶元素并更新栈顶元素的答案值
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[-1]*len(nums) # 没找到答案的则记录为-1
        stack=[]
        new_nums=2*nums
        for i in range(len(new_nums)):
            while stack and new_nums[i]>nums[stack[-1]]:
                ans[stack[-1]%len(nums)]=new_nums[i]
                stack.pop()
            stack.append(i%len(nums))
        return ans
        