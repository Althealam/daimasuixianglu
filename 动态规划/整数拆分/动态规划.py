# 分析：将数字n拆成m个数，并且希望这m个数尽可能的数值近似相等
# 动态规划五部曲
# 1. dp数组：分拆数字i，可以得到的最大乘积为dp[i]
# 2. 递推公式：
# 拆成两个数：对i的所有情况进行遍历，拆分后得到的为jx(i-j)
# 拆成两个数以上：jxdp[i-j]
# dp[i]=max(jx(i-j),jxdp[i-j],dp[i])
# 3. 初始化：dp[0]和dp[1]都为0（需要拆分为k个正整数的和，并且k>=2），dp[2]=1
# 4. 遍历顺序：dp[i]是依靠dp[i-j]的状态，因此遍历i是从前向后去遍历的，先有dp[i-j]再有dp[i]

# 时间复杂度：
# 1. 外层循环：O(n)
# 2. 内层循环：O(n)
# 总的时间复杂度：O(n^2)
# 空间复杂度：
# 1. dp数组的创建：O(n)
# 总的空间复杂度：O(n)

class Solution(object):
    # 假设对正整数i拆分出的第一个正整数是j（1<=j<i）
    # 1）将i拆分为j和i-j的和，且i-j不再继续拆分成多个正整数，此时的乘积是j*(i-j)
    # 2）将i拆分为j和i-j的和，且i-j继续拆分成多个正整数，此时的乘积是j*dp[i-j]
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[0]*(n+1) # 创建一个大小为n+1的数组在存储计算结果
        dp[2]=1 # 初始化dp[2]为1，因为当n=2时，只有一个切割方式1+1=2，乘积为1

        for i in range(3,n+1):
            # 遍历所有可能的切割点
            for j in range(1,n+1):
                # 计算切割点j与剩余部分i-j的乘积，并与之前的结果进行比较，取最大值
                dp[i]=max(dp[i],(i-j)*j,dp[i-j]*j)
        return dp[n] # 返回最终的计算结果
    
solution=Solution()
n=10
result=solution.integerBreak(n)
