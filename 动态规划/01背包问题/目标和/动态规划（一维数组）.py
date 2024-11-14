# 动态规划（一维dp）
# 分析：需要区分出一个正数的集合left，区分出一个负数的集合right
# left+right=sum, left-right=target
# right=sum-left, left-(sum-left)=target, left=(target+sum)/2（正数集合的值）
# 如果不能整除，那就是不能刚好凑出target

# 核心思想：本题是01背包问题，是问你将这个背包装满有几种方法
# 这个问题可以转化为这个形式：假设我们选择一些数字进行加法，另外一些数字进行减法，让这些加和减的结果恰好等于目标值S
# 由上面的分析，我们可以得到：我们需要找到一个子集，其和为(target+sum)/2

# 动态规划五部曲：
# 1. dp[j]：是否存在一个子集，其和恰好为j
# 2. 递推公式：对于每个元素nums[i]，我们从背包的容量target开始倒叙更新dp数组
# dp[j]=dp[j]+dp[j-nums[i]]
# 这表示我们在当前和为j-nums[i]的基础上，加上元素nums[i]，得到新的和为j的子集
# 3. 初始化：dp[0]=1，表示和为0的子集总是存在（即选择空子集）

# 时间复杂度：
# 1. sum(nums)：计算nums数组的总和，时间复杂度为O(n)
# 2. dp求解：O(n*target_sum), n是数组nums的长度，target_sum是计算得到的目标和
# 总的时间复杂度为O(nxtarget_sum)

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
        dp=[0]*(target_sum+1) # 创建动态规划数组，初始化为0
        dp[0]=1 # 当目标和为0的时候只有一种方案
        for num in nums:
            for j in range(target_sum,num-1,-1):
                dp[j]+=dp[j-num] # 状态转移方程，累加不同选择方式的数量
        return dp[target_sum] # 返回达到目标和的方案数
