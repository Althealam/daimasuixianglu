# 思路：
# 局部最优：只收集每天的正利润
# 全局最优：求得最大利润

# 1. diff[0]=nums[1]-nums[0]
# 2. diff[5]=nums[6]-nums[5]

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        diff=[0]*(len(prices)-1)
        for i in range(len(prices)-1):
            diff[i]=prices[i+1]-prices[i]
        return sum(item for item in diff if item>0)
        