# 本题求的是组合数而不是排列数（本题可以类比01背包中零一和的题目，递推公式的推导是一样的）
# 同时，本题的背包问题指的是装满这个背包有多少种方法，而且这个方法是组合数，没有顺序要求
# 动态规划五部曲
# 1. dp数组：dp[j]指的是装满背包容量为j的背包有dp[j]种方法
# 2. 递推公式：dp[j]+=dp[j-coins[i]]
# 3. 初始化：dp[0]=1（这是为了递推公式才设置为1的） 其他的dp为0
# 4. 遍历方法：先遍历物品，再遍历背包
# 先遍历背包，后遍历物品时得到的是排列数；而先遍历物品，后遍历背包得到的才是组合数

# 时间复杂度：
# 1. 外层循环：O(n)
# 2. 内层循环：O(amount)（内层循环的次数是amount-coins[i]+1）
# 总的时间复杂度是O(n*amount)
# 空间复杂度：
# 1. 动态规划数组：O(amount)
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp=[0]*(amount+1)
        dp[0]=1
        # 遍历物品
        for i in range(len(coins)):
            for j in range(coins[i],amount+1): # 后遍历背包
                dp[j]+=dp[j-coins[i]]
        return dp[amount]
        