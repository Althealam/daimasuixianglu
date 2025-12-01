# analysi: dp[sum(nums)//2]==sum(nums)//2 then the other bag is sum(nums)-sum(nums)//2=sum(nums)//2
# 1. definition of dp[i]: dp[i] means the maximal value of the bag when the volume is i
# 2. formula: target=sum(nums)//2
# (1) put j into bag: dp[i]=dp[i-nums[j]]+nums[j]
# (2) don't put j into bag: dp[i]=dp[i]
# 3. initialization: dp[i]=0
# 4. order: i left-right j right-left (element first then bag)

# 1. 为什么这个是01背包：01背包是物品只可以放入一次（每个数字只有两个选择，放或者不放） 而完全背包是物品可以无限次放入
# 2. 为什么01背包是先物品后背包：先物品后背包相当于是只使用前面i件物品时的最大背包容量，而先背包后物品则会导致物品重复出现
# 3. 为什么01背包遍历背包的时候要逆序：当我们想要在本轮使用物品i的时候，我们希望dp[j-nums[i]]的含义是上一轮中还没有使用nums[i]时的背包最大容量，当我们使用逆序的时候，dp[j-nums[i]]还没有被更新过。
# 如果我们使用正序，也就是for j in range(target)，那么此时dp[j-nums[i]]会变成正序，我们有可能已经在背包容量为j-nums[i]的时候使用过物品i了
# 4. 为什么使用逆序可以保证物品i不会被重复使用：当我们遍历到j的时候，此时正在更新dp[j]，而dp[j-nums[i]]中j-nums[i]<j，那么dp[j-nums[i]]就还没有被更新（更新顺序是j, j-1, ..., j-nums[i]）
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        target = sum(nums)//2
        dp=[0]*(target+1) # whether the elements can fulfill the bag?
        for i in range(len(nums)): # iterate elements
            for j in range(target, -1, -1): # iterate the volume of bag
                if j>=nums[i]:
                    dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])       
        if dp[target]==target:
            return True
        return False
        