# 方法：暴力法
# for循环适合模拟从头到尾的遍历，而while循环适合模拟环形遍历
# 时间复杂度：O(n^2)
# 空间复杂度：O(1)
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for i in range(len(cost)):
            rest=gas[i]-cost[i] # 记录剩余油量
            index=(i+1)%len(cost) # 下一个加油站的索引

            while rest>0 and index!=i: # 模拟以i为起点行驶一圈
                rest+=gas[index]-cost[index] # 更新剩余油量
                index=(index+1)%len(cost) # 更新下一个加油站的索引
            
            if rest>=0 and index==i: # 如果以i为起点跑一圈，剩余油量>=0，并且回到起始位置
                return i # 返回起始位置i
        return -1 # 所有起始位置都无法环绕一圈，返回-1
        