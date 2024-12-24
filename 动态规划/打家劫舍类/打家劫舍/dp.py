# 偷钱的规则是相邻房间不能偷
# 分析：某一个房间是否可以偷，依赖于前面两个房间的状态（偷、没偷）
# 1. dp数组的含义：考虑下标i（包含），所能偷的最大金币为dp[i]，结果数组为dp[len(nums)-1]
# 2. 递推公式：
# （1）偷i：dp[i-2]+nums[i]
# （2）不偷i：dp[i-1]
# dp[i]=max(dp[i-2]+nums[i],dp[i-1])
# 3. 初始化：dp[i]由dp[i-2]与dp[i-1]推导出来的
# （1）dp[0]=nums[0]
# （2）dp[1]=max(nums[0],nums[1])
# （3）对于i不等于0和1，则dp[i]=0
# 4. 遍历顺序：从前到后

# 时间复杂度：
# 1. 外层循环：从2遍历到len(nums)-1，时间复杂度为O(n)
# 2. 每次操作：执行max(dp[i-2]+nums[i],dp[i-1])，O(1)
# 总的时间复杂度为O(n)

# 空间复杂度：
# 1. dp数组：使用一个大小为len(nums)+1的数组dp来存储每个位置的最大金额，O(n)
# 总的空间复杂度为O(n)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[0]*(len(nums)+1)
        dp[0]=nums[0]
        if len(nums)>=2:
            dp[1]=max(nums[0],nums[1])

            for i in range(2,len(nums)):
                dp[i]=max(dp[i-2]+nums[i],dp[i-1])
         
        return dp[len(nums)-1]
