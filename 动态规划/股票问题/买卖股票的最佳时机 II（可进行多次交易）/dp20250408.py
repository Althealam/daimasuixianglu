class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits=[0]*(len(prices)-1)
        for i in range(len(prices)-1):
            profits[i]=prices[i+1]-prices[i]
        return sum([profit for profit in profits if profit>0])
        