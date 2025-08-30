# 思路：贪心，枚举从左到右卖出价格prices[i]时可以获得的最大利润
# 我们需要知道第i天之前，股票价格的最小值是多少，也就是从prices[0]到prices[i-1]的最小值，将它作为买入价格
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        ans = 0 # 最大利润
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            ans = max(ans, prices[i]-min_price)
        return ans