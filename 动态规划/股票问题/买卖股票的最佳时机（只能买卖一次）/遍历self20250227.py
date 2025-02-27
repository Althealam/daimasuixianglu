# 思路：选择买入价格最小的一天买入，选择卖出最大的一天卖出

# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=float('inf') # 一定要把min_price初始化为正无穷大，这样才能找到最小的profit
        max_profit=0
        if len(prices)==0:
            return 0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            if prices[i]-min_price>max_profit:
                max_profit=prices[i]-min_price
        return max_profit

        