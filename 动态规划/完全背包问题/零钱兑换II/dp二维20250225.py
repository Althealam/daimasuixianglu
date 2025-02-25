# 1. dp数组以及下标的含义：dp[i][j]表示用[0,i]的硬币凑满容量为j的背包，有dp[i][j]种方法
# 2. 递推公式
# （1）j<coins[i-1]：当前硬币面额大于当前目标金额，无法使用该硬币，dp[i][j]=dp[i-1][j]
# （2）j>=coins[i-1]：当前硬币金额大于当前目标金额，dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]
# 表示不使用当前硬币的方法数+使用当前硬币的方法数
# 本题的weight就是value
# 3. 初始化：二维dp数组的第一行的第一列一定要进行初始化
# （1）dp[0][j]：当j%coins[0]==0的时候，dp[0][j]=1
# （2）dp[i][0]：1
# 4. 遍历顺序：先遍历物品，后遍历背包

# 时间复杂度：O(m*n)，其中m是硬币的数量，n是目标金额
# 空间复杂度：O(m*n)，主要用于存储dp数组
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # 特殊情况判断
        if len(coins)==0:
            return 0
        coins.sort()
        if amount<coins[0]:
            return 1
        dp=[[0]*(amount+1) for _ in range(len(coins))]
        dp[0][0]=1
        # 初始化第一列，凑成金额0的方法为1
        for i in range(len(coins)): # i表示的是硬币的索引，因此不能使用len(coins)+1
        # 当i表示的不是硬币的索引的时候，才可以使用len(coins)+1
            dp[i][0]=1
        # 初始化第一行
        for j in range(1, amount+1):
            if j%coins[0]==0:
                dp[0][j]=1
        # 动态规划
        for i in range(1, len(coins)): # 遍历物品
            for j in range(1, amount+1): # 遍历背包
                if j<coins[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]
        return dp[-1][-1]
                

        