class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        leave = [0]*(len(gas))
        for i in range(len(gas)):
            leave[i] = gas[i]-cost[i]
        if sum(gas)<sum(cost):
            return -1
        start = 0 
        sum_ = 0
        for i in range(len(leave)):
            sum_+=leave[i]
            if sum_<0:
                start = i+1
                sum_=0
        return start

        