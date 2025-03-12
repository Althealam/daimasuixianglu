# 思路：
# 局部最优：只收集每天的正利润
# 全局最优：求得最大利润
# 分析：
# 1. 局部最优：在股票交易里，只要后一天的价格高于前一天的价格，就在这两天之间进行买卖，积累这些正利润就能达到局部最优，即每天都抓住了可盈利的机会
# 2. 全局最优：累计所有正的差值，就可以得到在整个时间序列里进行多次买卖所能获得的最大利润

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
        for i in range(len(diff)):
            diff[i]=prices[i+1]-prices[i]
        return sum(item for item in diff if item>0)