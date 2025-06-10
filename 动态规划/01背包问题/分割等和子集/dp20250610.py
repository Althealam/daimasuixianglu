# 1. dp数组以及下标的含义：dp[j]表示装满容量为j的背包时的最大价值为dp[j]
# 当dp[target]==target的时候，说明可以装满，则返回True
# 2. 递推公式：
# （1）放入物品i：dp[j]=dp[j-weight[i]]+value[i]
# （2）不放入物品i：dp[j]
# 由于weight和value是相同的
# 因此：dp[j]=max(dp[j-nums[i]]+nums[i], dp[j]) j>=nums[i]
# 3. 初始化：dp[0]=0
# 4. 遍历顺序：先物品后背包，背包逆序


nums=list(map(int, input().split()))

def ditui(nums):
    if sum(nums)%2!=0:
        return False
    target=sum(nums)//2
    # print(target)
    dp=[0]*(target+1)
    for i in range(len(nums)): # 遍历物品   
        for j in range(target, -1, -1): # 遍历背包
            if j>=nums[i]:
                dp[j]=max(dp[j], dp[j-nums[i]]+nums[i])
    # print(dp)
    if dp[target]==target:
        return True
    return False

result=ditui(nums)
print(result)