# 动态规划五部曲（需要输出最长递增子序列的长度）
# 1. dp数组：dp[i]是以nums[i]为结尾（包括i）的最长递增子序列的长度
# 2. 递推公式：
# 位置i的最长升序子序列等于j从0到i-1个个位置的最长升序子序列+1的最大值
# 如果nums[i]>nums[j]：dp[i]=max(dp[j]+1,dp[i])
# 3. 初始化：dp[i]=1（至少包含i）
# 4. 遍历顺序：从小到大遍历（递增，dp[i]依赖于前面的dp[j]）

# 时间复杂度：
# 1. 外层循环：O(n)
# 2. 内层循环：O(i)
# 时间复杂度：O(n^2)
# 空间复杂度：
# 1. dp数组：存储以每个元素结尾的最长递增子序列的长度
# 空间复杂度：O(n)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[1]*len(nums)
        result=1
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
            result=max(result,dp[i])
        return result

        