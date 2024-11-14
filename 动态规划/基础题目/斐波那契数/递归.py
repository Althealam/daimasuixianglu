# 方法：dp法（精简版）
# 分析：
# 动态规划五部曲
# 1. 确定dp[i]的含义：dp[i]表示第i个斐波那契数值为dp[i]
# 2. 确定递推公式：dp[i]=dp[i-1]+dp[i-2]
# 3. dp数组的初始化：dp[0]=0, dp[1]=1
# 4. 确定遍历顺序：从前向后遍历，这样可以保证每次的dp[i]都是由最新的dp[i-1]和dp[i-2]计算而来的
# 5. 打印dp数组（用于debug）

# 时间复杂度：
# 1. 递归调用：递归树的高度为O(n)
# 2. 重复计算：递归树的节点数大约为2^n，因此为O(2^n)
# 总的时间复杂度：O(2^n)
# 空间复杂度：
# 1. 递归栈空间：O(n)
# 2. 其他空间：无
# 总的空间复杂度：O(n)
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return n
        return self.fib(n-1)+self.fib(n-2)     