# 暴力解法（超出时间限制）
# 关键点：1. 总和大于等于target 2. 长度最小
# 思路：利用一个i循环遍历nums，利用一个j遍历i后面的元素，然后依次叠加nums[j]的值，判断sum是否大于target，如果大于了，就记录下来此时的窗口大小，也就是数组长度，并且和min_length（将min_length初始化为无穷大）进行比较，如果比min_length小的话就更新min_length
# 空间复杂度：O(1)
# 时间复杂度：O(n^2)
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i=0
        min_length=float('inf') # 无穷大
        for i in range(len(nums)):
            cur_sum=0 # 用来记录这次遍历的数组之和
            for j in range(i,len(nums)):
                cur_sum+=nums[j]
                if cur_sum>=target:
                    min_length=min(min_length,j-i+1)
                    break
        return 0 if min_length==float('inf') else min_length
                    
solution=Solution()
target=4
nums = [1,4,4]
result=solution.minSubArrayLen(target,nums)