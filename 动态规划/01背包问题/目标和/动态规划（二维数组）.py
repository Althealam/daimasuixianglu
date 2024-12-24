# 动态规划（二维dp）
# 分析：需要区分出一个正数的集合left，区分出一个负数的集合right
# left+right=sum, left-right=target
# right=sum-left, left-(sum-left)=target, left=(target+sum)/2（正数集合的值）
# 如果不能整除，那就是不能刚好凑出target

# 核心思想：本题是01背包问题，是问你将这个背包装满有几种方法
# 这个问题可以转化为这个形式：假设我们选择一些数字进行加法，另外一些数字进行减法，让这些加和减的结果恰好等于目标值S
# 由上面的分析，我们可以得到：我们需要找到一个子集，其和为(target+sum)/2

# 动态规划五部曲：
# 1. dp[i][j]：使用下标为[0,]的nums[i]能够凑满j容量的包，有nums[i][j]种方法
# 2. 递推公式：
# （1）不放物品i：即背包容量为j，里面不放物品i，装满有dp[i-1][j]种方法
# （1）放物品i：先空出物品i的容量，背包容量为j-weights[i]，放满背包有dp[i-1][j-weights[i]]种方法
# 综上，递推公式为dp[i][j]=dp[i-1][j]+dp[i-1][j-weights[i]]（本题物品i的容量是nums[i]，价值也是nums[i]）
# 3. 初始化：初始化第一行和第一列，已知dp[0][0]=1，即装满背包容量为0的方法数量是放0件物品
# （1）dp[0][j]：只放物品0，把容量为j的背包填满有几种方法
# dp[0][nums[0]]=1，其他为0
# （2）dp[i][0]：背包容量为0，把物品0到物品i，装满有几种方法：dp[i][0]=1


# 时间复杂度：
# 1. sum(nums)：O(n)
# 2. 动态规划数组dp：O(n*target_sum)
# 总的时间复杂度为O(n*target_sum)

# 空间复杂度：
# 1. dp数组：O(target_sum)
# 总的空间复杂度为O(target_sum)
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

        # 创建二维动态规划数组，行表示选取的元素数量，列表示累加和
        dp = [[0] * (target_sum + 1) for _ in range(len(nums) + 1)]

        # 初始化状态
        dp[0][0] = 1

        # 动态规划过程
        for i in range(1,len(nums)+1):  # 遍历物品
            for j in range(target_sum+1): # 遍历背包
                dp[i][j]=dp[i-1][j] # 不选取当前元素
                if j>=nums[i-1]:
                    dp[i][j]+=dp[i-1][j-nums[i-1]] # 选取当前元素
        return dp[len(nums)][target_sum] # 达到目标和的方案数
