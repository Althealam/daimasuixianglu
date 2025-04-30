class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=[0]*(len(prices)-1)
        profit=0
        for i in range(len(prices)-1):
            result[i]=prices[i+1]-prices[i]
            if result[i]>0:
                profit+=result[i]
        return profit
        