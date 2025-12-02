# analysis: suppost target=a-b sum=a+b ==> a=b+target, 2b+target=sum ==> b=(sum-target)/2 a=(sum+target)/2
# 1. definition: dp[i] denotes the number of different expressions that the sum of arrays can be i, then dp[target_sum] is our answer 
# 2. formula: 
# (1) use nums[i]: dp[j]+=dp[j-nums[i]]
# (2) don't use nums[i]: dp[j]
# 3. initialization: dp=[0]*(target_sum+1) dp[0]=1 
# 4. order: 01package, then element first then package

# 为什么一定要初始化为dp[0]=1：表示凑出0的时候方案数为1个。如果不做初始化的话，递推无法成功
# 因为当j=num的时候，dp[num]+=dp[0]，表示直接使用一个num就可以凑出一个方案
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (sum(nums)+target)%2!=0:
            return 0
        target_sum = (sum(nums)+target)//2
        if target_sum+1<0:
            return 0
        dp = [0]*(target_sum+1)
        dp[0] = 1
        for num in nums: # iterate nums
            for j in range(target_sum, -1, -1): # iterate package
                if j>=num:
                    dp[j]+=dp[j-num]
        return dp[-1]