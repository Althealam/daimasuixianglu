# 思路：用i%len(nums)的思路来进行处理，不需要进行拼接

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dp=[-1]*len(nums)
        stack=[0]
        for i in range(1, len(nums)*2):
            while stack and nums[i%len(nums)]>nums[stack[-1]]:
                dp[stack[-1]]=nums[i%len(nums)]
                stack.pop()
            stack.append(i%len(nums))
        return dp