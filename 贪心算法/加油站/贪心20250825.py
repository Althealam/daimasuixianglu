class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        res = [0]*len(gas)
        for i in range(len(gas)):
            res[i] = gas[i]-cost[i]
        
        sum_= 0 # 从ans出发时的油耗累加和
        ans = 0 # 出发的编号
        for i in range(len(res)):
            sum_+=res[i]
            if sum_<0:
                ans = i+1
                sum_=0

        return ans