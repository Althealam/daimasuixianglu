class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = [0]*len(gas)
        for i in range(len(gas)):
            ans[i] = gas[i]-cost[i]
        if sum(ans)<0:
            return -1
        sum_ = 0
        res = 0
        for i in range(len(ans)):
            sum_+=ans[i]
            if sum_<0:
                sum_=0
                res=i+1
        return res
