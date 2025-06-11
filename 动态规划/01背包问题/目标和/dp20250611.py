# 推导: a+b=sum(nums) a-b=target ==> a=(sum(nums)+target)//2
# 1. dp数组以及下标的含义：装满容量为j的背包有dp[j]种方法
# 2. 递推公式：
# （1）不放入物品i：dp[j]
# （2）放入物品i：dp[j-nums[i]]
# dp[j]=dp[j]+dp[j-nums[i]]==>dp[j]+=dp[j-nums[i]]
# 3. 初始化：dp[0]=1
# 4. 遍历顺序：先物品后背包，背包逆序

nums=list(map(int, input().split()))
s=int(input())

def ditui(nums, s):
    if (sum(nums)+s)%2!=0:
        return 0 # 此时没有方案
    if abs(s)>sum(nums):
        return 0
    target=(sum(nums)+s)//2
    dp=[0]*(target+1)
    dp[0]=1
    for num in nums: # 遍历物品
        for j in range(target, num-1, -1): # 遍历背包
            dp[j]+=dp[j-num]
    return dp[target]

result=ditui(nums, s)
print(result)