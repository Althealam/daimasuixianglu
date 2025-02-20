# 1. dp数组的含义以及下标：dp[i]表示第i个数的斐波那契数为dp[i]
# 2. 递推公式：dp[i]=dp[i-1]+dp[i-2]
# 3. dp数组的初始化：dp[0]=0, dp[1]=1
# 4. 遍历顺序：从左到右
# 5. 举例推导dp数组

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 特殊情况
        if n==0:
            return 0
        
        # 创建dp数组
        dp=[0]*(n+1)

        # 初始化dp数组
        dp[0]=0
        dp[1]=1

        # 遍历顺序，从前向后
        for i in range(2, n+1):
            dp[i]=dp[i-1]+dp[i-2]
        
        # 返回答案
        return dp[n]