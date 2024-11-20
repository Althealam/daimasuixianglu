# 思路：将两个数组拼在一起，可以模拟两个数组首尾相连，然后只要取前面的len(nums)个元素的result即可
# 时间复杂度：
# 1. 主循环：遍历了2n次，其中n是nums的长度
# 2. 内层循环：每个元素最多会被压入栈一次并从栈中弹出一次，因此内层while循环的总执行次数为O(n)
# 总的时间复杂度为O(n)
# 空间复杂度：
# 1. 栈：栈用于存储数组索引，最坏情况下栈中可能同时存在所有元素的索引，空间复杂度为O(n)
# 2. 结果数组dp：存储结果，占用O(n)的空间
# 3. 其他变量为O(1)
# 总的空间复杂度为O(n)


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dp=[-1]*len(nums)
        stack=[]
        for i in range(len(nums)*2):
            while (len(stack)!=0 and nums[i%len(nums)]>nums[stack[-1]]):
                dp[stack[-1]]=nums[i%len(nums)]
                stack.pop()
            stack.append(i%len(nums))
        return dp