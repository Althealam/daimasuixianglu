# 和零钱兑换II的区别：零钱兑换II是组合，组合总和IV是排列
# 1. 先遍历物品再遍历背包得到的是组合数
# 2. 再遍历背包再遍历物品得到的是排列数

# 时间复杂度：
# 1. 外层循环：target次迭代
# 2. 内层循环：len(nums)次迭代，假设len(nums)=n
# 总的时间复杂度为O(n*target)
# 空间复杂度：
# 1. 动态规划数组：使用一个长度为target+1的数组dp来保存每个目标金额i的组合数
# 空间复杂度为O(target)
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp=[0]*(target+1)
        dp[0]=1

        for i in range(1,target+1): # 遍历背包
            for j in range(len(nums)): # 遍历物品
                if i-nums[j]>=0:
                    dp[i]+=dp[i-nums[j]]
        
        return dp[target]
        