# 1. dp数组以及下标的含义：dp[j]表示组合总和为j的时候组合数为dp[j]
# 2. 递推公式：
# （1）使用num：dp[j-num]
# （2）不实用num：dp[j]
# dp[j]+=dp[j-num]
# 3. 初始化：dp[0]=1
# 4. 遍历顺序：先背包后物品，因为本题是求排列数
nums=list(map(int, input().split()))
target=int(input())

def ditui(target, nums):
    dp=[0]*(target+1)
    dp[0]=1
    for j in range(target+1):
        for num in nums:
            if j>=num:
                dp[j]+=dp[j-num]
    return dp[-1]

result=ditui(target, nums)
print(result)