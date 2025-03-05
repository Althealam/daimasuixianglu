# 思路：将两个nums拼接起来进行判断 new_nums=nums+nums
# 1. 定义单调栈stack，用来记录左边第一个比他大的元素的下标是多少
# 2. 遍历new_nums：
# （1）new_nums[i]<new_nums[stack[-1]]: stack.append(i)
#  (2) new_nums[i]>=new_nums[stack[-1]]: answer[stack[-1]]=new_nums[i] stack.pop() stack.append(i)
# 最后返回的是answer[:len(nums)]

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_nums=nums+nums
        stack=[0]
        answer=[-1]*len(new_nums)
        for i in range(1, len(new_nums)):
            if new_nums[i]<=new_nums[stack[-1]]:
                stack.append(i)
            else:
                while stack and new_nums[i]>new_nums[stack[-1]]:
                    answer[stack[-1]]=new_nums[i]
                    stack.pop()
                stack.append(i)
        return answer[:len(nums)]
        