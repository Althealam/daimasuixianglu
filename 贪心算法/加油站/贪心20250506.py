# 思路：
# 1. 特殊情况判断：判断sum(gas)>=sum(cost)，否则直接返回-1
# 2. 计算gas[i]-cost[i]，然后从i=0的地方出发累加，判断是否会出现值为小于0的情况，如果没有的话则0是出发点，如果有的话则非0是出发点
# 3. 从非0的位置出发，每次都计算sum_是否小于0，如果是的话则start=i+1并且更新sum_，如果不是的话则继续累加油量
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        nums=[0]*len(gas) # 统计不同的位置的油量的消耗
        for i in range(len(gas)):
            nums[i]=gas[i]-cost[i]
        # 寻找出发位置
        sum_=0 # 油量
        start=0 # 出发位置
        for i in range(len(nums)):
            sum_+=nums[i]
            if sum_<0:
                start=i+1
                sum_=0
        return start
        