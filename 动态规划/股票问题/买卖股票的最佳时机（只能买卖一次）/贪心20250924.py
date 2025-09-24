class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        ans = 0 
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            ans = max(ans, prices[i]-min_price)
        return ans
        