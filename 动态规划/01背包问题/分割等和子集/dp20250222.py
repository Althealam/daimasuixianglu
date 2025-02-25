# 本题的nums中的值是value也是weight
# 1. dp数组及其下标的含义：dp[i]表示装满容量为i的背包后的最大价值为dp[i]
# 当dp[i]=i的时候，背包就装满了（因为本题的i是value也是target）
# 2. 递推公式：dp[i]=max(dp[i-1], dp[i-nums[j]]+nums[j])
# （1）容量为i的背包不放入数组nums[j]时的最大价值：dp[i-1]
# （2）容量为i的背包放入数组nums[j]时的最大价值：dp[i-nums[j]]+nums[j]
# 3. 初始化：dp[0]=0（如果value有负数，则非0下标就要初始化为负无穷）
# 4. 遍历顺序：一维dp数组，物品遍历的for循环放在外层，背包遍历的for循环放在内层，并且遍历背包的时候要从右到左，遍历物品的时候要从左到右
# 如果遍历背包的时候从左到右遍历，会出现一个物品被重复使用的情况

# 时间复杂度：O(n*target)，n是nums的长度，target是目标和
# 需要遍历数组中的每个元素，并且对于每个元素，需要更新从target到该元素大小的dp数组的和
# 空间复杂度：O(target)，存储一维数组


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 如果总和为奇数，那么无法将数组分成两个和相等的子集，直接返回False
        if sum(nums)%2!=0:
            return False
        
        target=sum(nums)//2 # 目标和

        dp=[0]*(target+1) # dp[i]表示装满容量为i的背包所能获得的最大价值，本题中元素的价值也是元素的容量

        for num in nums: # 遍历物品
            # 遍历背包（从目标容量开始递减到当前物品的容量）
            for j in range(target,  num-1, -1):
                dp[j]=max(dp[j], dp[j-num]+num)
                # （1）不放入nums：dp[j]
                # （2）放入nums：dp[j-num]+num
        
        # 判断是否装满了背包容量为target的背包
        if dp[target]==target:
            return True
        else: 
            return False
        