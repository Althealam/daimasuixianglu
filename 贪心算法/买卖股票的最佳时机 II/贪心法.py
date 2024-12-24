# 方法：贪心法
# 思路：局部最优：收集每天的正利润；全局最优：求得最大利润
# 收集正利润的区间，就是股票买卖的区间，而我们只需要关注最终利润，不需要记录区间

# 时间复杂度：
# 代码的操作是从索引1到len(prices)-1的for循环，并且在每次迭代中，计算prices[i]-prices[i-1]和max操作都是常数时间
# 总的时间复杂度为O(n)
# 空间复杂度：
# 代码只用了一个变量result来累加结果
# 总的空间复杂度为O(1)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result=0
        for i in range(1,len(prices)):
            result+=max(prices[i]-prices[i-1],0)
        return result
        