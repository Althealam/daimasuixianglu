# 思路：
# 1. 如果gas的总和小于cost的总和，那么无论从哪里出发，都没办法跑完一圈；
# 2. rest[i]=gas[i]-cost[i]为一天剩下的有，i从0开始计算累加到最后一站，如果累加没有出现负数，说明从0开始，油没断过，那么0就是起点；
# 3. 如果累加的最小值是负数，那么汽车就要从非0节点开始出发

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        # 1. 判断是否可以跑完全程
        if sum(gas)<sum(cost):
            return -1
        
        # 2. 计算每个加油站的油耗
        rest=[None]*len(gas)
        min_gas=float('inf')
        # 计算每个加油站的剩余油量
        for i in range(len(gas)):
            rest[i]=gas[i]-cost[i]
            if rest[i]<min_gas:
                min_gas=rest[i]
        
        # 3. 如果最小的剩余油量都是大于等于0的，说明从0开始即可
        if min_gas>=0:
            return 0
        
        # 4. 如果最小的剩余油量是小于0的，那么就不是从0开始
        curSum=0 # 目前的总油量，需要确保从start加油站开始的路途中的总油量一直是大于等于0的
        for i in range(0,len(rest)):
            curSum+=rest[i]
            if curSum<0:
                start=i+1
                curSum=0
        return start
        