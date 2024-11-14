# 分析：
# 动态规划五部曲
# 1. 确定dp[i]的含义：dp[i]表示第i个斐波那契数值为dp[i]
# 2. 确定递推公式：dp[i]=dp[i-1]+dp[i-2]
# 3. dp数组的初始化：dp[0]=0, dp[1]=1
# 4. 确定遍历顺序：从前向后遍历，这样可以保证每次的dp[i]都是由最新的dp[i-1]和dp[i-2]计算而来的
# 5. 打印dp数组（用于debug）
# 时间复杂度：O(n)
# 1. 初始化dp数组：O(n)
# 2. 循环计算Fibonacci数列：O(n)
# 空间复杂度：O(n)
# 1. dp数组：O(n)
# 2. 其他辅助变量：O(1)
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1 # 初始化
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2] # 递推公式
        return dp[n]        