nums = list(map(int, input().split()))

# 1. dp数组以及下标的含义：dp[i]表示[0,i-1]的数组范围内的最大子数组和为dp[i]
# 2. 递推公式
# （1）不重新开始：dp[i-1]+nums[i]
# （2）重新开始：nums[i]
# dp[i]=max(dp[i-1]+nums[i], nums[i])
# 3. 初始化：全部初始化为0
def ditui(nums):
    if len(nums)==1:
        return nums[0]
    dp=[0]*len(nums)
    dp[0]=nums[0]
    result=nums[0]
    for i in range(1, len(nums)):
        dp[i]=max(dp[i-1]+nums[i], nums[i])
        result=max(result, dp[i])
    return result 

result=ditui(nums)
print(result)