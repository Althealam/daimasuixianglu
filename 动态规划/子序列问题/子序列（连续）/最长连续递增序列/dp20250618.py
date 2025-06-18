# 1. dp数组以及下标的含义：dp[i]表示以nums[i]为结尾的连续递增子序列的长度
# 2. 递推公式：
# 如果nums[i]>nums[i-1]：dp[i]=dp[i-1]+1
# 如果nums[i]<=nums[i-1]: dp[i]=1
# 3. 初始化：全部初始化为1
# 4. 遍历顺序：从前向后遍历

nums = list(map(int, input().split()))

def ditui(nums):
    dp=[1]*len(nums)
    for i in range(1, len(nums)):
        if nums[i]>nums[i-1]:
            dp[i]=dp[i-1]+1
    return max(dp)

result=ditui(nums)
print(result)