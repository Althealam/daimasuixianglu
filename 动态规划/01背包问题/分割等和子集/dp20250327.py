# 1. dp数组以及下标的含义：dp[j]表示装满容量为j的背包，所背的物品价值最大为dp[j]
# 当dp[i]=i的时候，背包就装满了
# 2. 递推公式：dp[j]=max(dp[j], dp[j-nums[i]]+nums[i])
# （1）不装物品i：dp[j]
# （2）装物品i：dp[j-nums[i]]+nums[i]
# 3. 初始化：dp[0]=0
# 4. 遍历顺序：先物品后背包（对于一维dp数组是如此，否则会出现重复的情况）
# 并且遍历背包时要从右到左

nums=[2,2,1,1]

class Solution:
    def canPartition(self, nums) -> bool:
        if sum(nums)%2!=0:
            return False
        target=sum(nums)//2

        dp=[0]*(target+1)
        for num in nums: # 先遍历物品
            for j in range(target, num-1, -1): # 遍历背包（从右到左，并且确保大于num）
                dp[j]=max(dp[j], dp[j-num]+num)
        print(dp)
        if dp[target]==target:
            return True
        else:
            return False
        
        
sol=Solution()
print(sol.canPartition(nums))