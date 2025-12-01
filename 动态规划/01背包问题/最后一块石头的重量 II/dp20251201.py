# analysis: suppost the first weight of stones is s, then the other weight of stones is sum(stones)-s
# then the weight of the left stone is abs(s-(sum(stones)-s))=abs(2s-sum(stones))
# 1. definition: dp[i] denotes the maximal value of the numbers when using the first i stones
# 2. formula: dp[j] = max(dp[j-stones[i]]+stones[i], dp[j]) 
# 3. innitilization: all initialize as 0
# 4. order: stones first then volume
# return: sum(nums)-2*dp[target]
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones)//2
        dp = [0]*(target+1)
        for stone in stones: # iterate stone
            for j in range(target, -1, -1): # iterate volume
                if j>=stone:
                    dp[j] = max(dp[j-stone]+stone, dp[j])
        return sum(stones)-2*dp[-1]