# 方法：贪心法
# 分析：计算每个点i的gas[i]-cost[i]的值，这个值就是每个站点剩余的油量，将这个数组记录假设为num
# 如果num的前面k个累加值current_sum<0，那就说明前面k个点作为出发点的话，都没办法跑完一圈，那么我们就选择k+1作为我们的起始值
# 记录total_sum，total_sum是前面gas[i]-cost[i]的所有数组之和，如果total_sum<0的话，说明不管从哪个起点开始跑，都不可能跑完一圈，因为整体的消耗就是小于0的

# 时间复杂度：
# 遍历gas和cost，每次迭代中的操作都是常数时间，因此时间复杂度为O(n)
# 空间复杂度：
# 只使用了常数个额外变量curSum、totalSum和start，因此空间复杂度为O(1)
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        curSum=0 # 当前累计的剩余油量
        totalSum=0 # 总剩余油量
        start=0
        for i in range(len(gas)):
            curSum+=gas[i]-cost[i]
            totalSum+=gas[i]-cost[i]

            if curSum<0: # 当前累计剩余油量curSum<0
                start=i+1 # 起始位置更新
                curSum=0 # curSum重新从0开始记录
        
        # 总的剩余油量<0，说明无论从哪个起点开始，都无法环绕一圈
        if totalSum<0:
            return -1
        return start
