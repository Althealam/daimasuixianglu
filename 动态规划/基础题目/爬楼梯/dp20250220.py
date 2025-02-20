# 1. dp数组的含义及下标：dp[i]表示爬到第i阶有dp[i]种方法
# 2. 递推公式：
# （1）如果爬到了i-1，那么再爬一层即可，那就是dp[i-1]个方法
# （2）如果爬到了i-2，那么再爬两层即可，那么就是dp[i-2]个方法
# dp[i]=dp[i-1]+dp[i-2]
# 3. dp数组的初始化：dp[0]=1 dp[1]=1
# dp[0]必须是1，否则dp[2]不好推导出来，因为dp[2]实际上有两种方法
# 4. 遍历顺序：从左到右

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 特殊情况判断
        if n==0:
            return 1
        # 初始化
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        