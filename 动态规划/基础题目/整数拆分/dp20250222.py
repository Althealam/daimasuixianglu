# 1. dp数组以及下标的含义：dp[i]表示拆分数字i，可以得到的最大乘积为dp[i]
# 2. 确定递推公式：
# 定义j为从i中拆分出来的正整数，那么j的范围是1<=j<=i-1
# 因此i=j+(i-j)
# 那么dp[i]的值有以下两种可能：
# （1）dp[i]=j*(i-j) （2）dp[i]=j*dp[i-j]（将i-j进行拆分）
# 第一种情况是将整数直接拆分为2个整数；第二种情况是将整数拆分为多个整数
# 那么 dp[i]=max(j*(i-j), j*dp[i-j], dp[i])
# 3. 初始化：dp[0]=0 dp[1]=1 dp[2]=1(2=1+1，因此dp[2]=1)
# 4. 遍历顺序：从左到右

# 时间复杂度：O(n^2)
# 空间复杂度：O(n)

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1) # 创建一个大小为n+1的数组来存储u计算结果
        dp[0]=0
        dp[1]=1
        dp[2]=1 # 2应该拆分为1+1，因此乘积为1
        for i in range(3, n+1):
            for j in range(1, i): # j表示拆分出的一个正整数，从1到i-1结束
                dp[i]=max(dp[i],j*(i-j), j*dp[i-j])
        
        return dp[n]