# nums=list(map(int, input().split()))
# target=int(input())
# 1. dp数组以及下标的含义：dp[i]表示凑成目标正整数i的排列个数为dp[i]
# 2. 递推公式：
# （1）考虑nums[i]: dp[i]+=dp[i-nums[i]]
# （2）不考虑nums[i]：dp[i]=dp[i-1]
# 3. 初始化：dp=[0]*target dp[0]=1
# 4. 遍历顺序：先物品后背包，背包逆序


# 时间复杂度：O(targetxn)
# 空间复杂度：O(target)

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp=[0]*(target+1)
        dp[0]=1
        for j in range(1, target+1): # 先遍历背包
            for num in nums: # 后遍历物品
                if j>=num:
                    dp[j]+=dp[j-num]
        return dp[target]