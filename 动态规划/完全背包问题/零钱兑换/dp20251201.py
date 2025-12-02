# 1. definition: dp[j] denotes the fewest number of coins that we need to make up that amount
# 2. formula:
# (1) use coin: dp[j-coin]+1
# (2) don't use coin: dp[j]
# dp[j] = min(dp[j-coin]+1, dp[j])
# 3. initialization: dp = [float('inf')]*(amount+1)
# dp[0] = 0
# 4. order: full package, combination number, element first package then

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for j in range(amount+1):
                if j>=coin:
                    dp[j] = min(dp[j-coin]+1, dp[j])
        return dp[-1] if dp[-1]!=float('inf') else -1