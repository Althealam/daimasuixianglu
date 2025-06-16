# 1. dp数组以及下标的含义：dp[i]表示偷窃[0, i]的nums时的最高金额为dp[i]
# 2. 递推公式：
# （1）偷i：dp[i-2]+nums[i]
# （2）不偷i：dp[i-1]
# dp[i]=max(dp[i-2]+nums[i], dp[i-1])
# 3. 初始化：dp[0]=nums[0] dp[1]=max(nums[0], nums[1])
# 4. 遍历顺序：从前向后

nums=list(map(int, input().split()))

def ditui(nums):
    # 1. 偷头不偷尾
    result1=robrange(nums[:len(nums)-1])
    # 2. 偷尾不偷头
    result2=robrange(nums[1:])
    return max(result1, result2)

def robrange(nums):
    if len(nums)==0:
        return 0
    if len(nums)==1:
        return nums[0]
    dp=[0]*len(nums)
    dp[0]=nums[0]
    dp[1]=max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i]=max(dp[i-1], dp[i-2]+nums[i%len(nums)])
    print(dp)
    return dp[-1]

result=ditui(nums)
print(result)

