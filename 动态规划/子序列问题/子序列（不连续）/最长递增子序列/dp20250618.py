# 1. dp数组以及下标的含义：dp[i]表示以nums[i]为结尾的最长递增子序列的长度
# 2. 递推公式：位置i的最长子序列长度为0到i-1的最长递增子序列长度加1
# if nums[i]>nums[j]: dp[i]=dp[j]+1
# 3. 初始化：dp[i]=1
# 4. 遍历顺序：先遍历i，再遍历j

nums = list(map(int, input().split()))

def ditui(nums):
    dp=[1]*len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i]=max(dp[i], dp[j]+1)
    return max(dp)