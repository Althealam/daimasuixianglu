# 1. dp数组以及下标的含义：dp[i]表示i之前包括i的以nums[i]结尾的最长递增子序列
# 2. 递推公式：if nums[i]>nums[j]: dp[i]=max(dp[i], dp[j]+1)
# 位置i的最长递增子序列等于j从0到i-1各个位置的最长递增子序列的长度+1
# 3. 初始化：dp[i]=1 （至少包含自己一个元素）
# 4. 遍历顺序：i的循环在外层，j的循环在内层

# 时间复杂度：O(n^2)
# 空间复杂度：O(n)

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[1]*len(nums)
        result=1 # 记录最长递增子序列的长度
        # 注意：最长递增子序列不一定会包含nums[len(nums)-1]的，因此不能返回dp[len(nums)-1]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i], dp[j]+1)
                    result=max(result, dp[i])
        return result
        