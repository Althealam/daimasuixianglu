# 1. definition: dp[i][0] means the maximal profit you can achieve when you have the stock for the first time, dp[i][1] means the maximal profit you can achieve when you don't have the stock for the first time
# dp[i][j]=have the stock if j%2==0, else dp[i][j]=don't have the stock
# 2. formula:
# (1) if j%2==0, then you have the stock: dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]-prices[i])
# (2) elif j%2!=0, then you don't have the stock: dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+prices[i])
# 3. initialization: you can buy at most k times and sell at most k times, so there are 2*k states totally
# dp=[[0]*2*k for _ in range(len(prices))]
# dp[0][j]=-prices[0] if j%2==0 else dp[0][j]=0
# dp[i][0] = max(dp[i-1][0], -nums[0])
# 4. order: iterate prices and then iterate k
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp=[[0]*2*k for _ in range(len(prices))]
        for j in range(2*k):
            if j%2==0:
                dp[0][j]=-prices[0]
        for i in range(1, len(prices)):
            for j in range(2*k):
                if j==0: # you have the stock for the first time
                    dp[i][0] = max(dp[i-1][j], -prices[i])
                elif j%2==0: # you have the stock for the j%2 time
                    # we need to intialize the dp[i][0] because j>=1
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]-prices[i])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+prices[i])
        return dp[-1][-1]



        