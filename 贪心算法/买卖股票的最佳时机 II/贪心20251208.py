# 只要今天的价格比昨天的高，你就可以去累计收益
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = [0]*(len(prices)-1)
        for i in range(len(prices)-1):
            ans[i] = prices[i+1]-prices[i]
        return sum(x for x in ans if x>=0)