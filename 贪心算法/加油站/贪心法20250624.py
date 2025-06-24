# 思路：
# 1. 特殊情况判断：判断gas的和是否大于等于cost，如果小于的话说明不管从哪里出发都不能跑完，那么直接返回-1
# 2. 如果上述判断通过后，则进行下一步，求出每个节点的油耗
# 从0开始出发累加油耗，如果发现有一步的油耗累加和小于0，则从下一个地方开始，更新累加和和答案值
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        res = [0]*len(gas)
        for i in range(len(gas)):
            res[i]=gas[i]-cost[i]
        
        sum_=0 # 从ans出发时的油耗累加和
        ans =0 # 出发的编号
        for i in range(len(res)):
            sum_+=res[i]
            if sum_<0:
                ans = i+1
                sum_=0
                
        
        return ans