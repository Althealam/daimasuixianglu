# 分析：假设加法的总和是x，那么减法的总和就是sum(nums)-x
# 我们需要x-(sum(nums)-x)==target： x=(target+sum)/2

# 1. dp数组的下标及其含义：dp[i][j]使用下标[0,i]的nums[i]能够凑满容量为j的书包，并且有dp[i][j]种方法
# 2. 递推公式：dp[i][j]=dp[i-1][j]+dp[i-1][j-nums[i]]
# （1）不放物品i：dp[i][j]=dp[i-1][j]
# （2）放物品i：dp[i-1][j-nums[i]]
# 3. dp数组的初始化：第一行和第一列一定需要初始化
# dp[0][j]：只放物品0，把容量为j的背包填满的方法 dp[0][nums[0]]=1 dp[0][j]=0(j!=nums[0])
# dp[i][0]：背包容量为0，放0件物品
# 4. 遍历顺序：从上到下，从左到右（当前值是由上方和左上方推出来的）

# 时间复杂度：O(nxtarget_sum)
# 空间复杂度：O(nxtarget_sum)

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        total_sum=sum(nums) # 计算nums的总和
        if abs(target)>total_sum:
            return 0 # 此时没有方案

        if (target+total_sum)%2==1:
            return 0 # 此时没有方案
        
        target_sum=(target+total_sum)//2 # 目标和

        # 创建dp数组
        dp=[[0]* (target_sum+1) for _ in range(1+len(nums))]
        # 初始化状态
        dp[0][0]=1

        for i in range(1, len(nums)+1): # 遍历物品
            for j in range(target_sum+1): # 遍历背包
                dp[i][j]=dp[i-1][j]
                if j>=nums[i-1]:
                    dp[i][j]+=dp[i-1][j-nums[i-1]]
        
        return dp[len(nums)][target_sum] # 返回达到目标和的方案数

        