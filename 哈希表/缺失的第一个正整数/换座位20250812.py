# 换座位法：假设位置i的学生的学号为nums[i-1]，那么位置nums[i]的学生的学号为nums[nums[i]-1]（因为学号是从1开始的，而不是从0开始的）
# 遍历每个座位，将学生按照其学号交换位置。比如位置i上坐的学生的学号是nums[i]，那么将nums[i]交换到nums[nums[i]-1]的位置上
# 最后遍历所有的nums，判断是否有哪个位置出现i!=nums[i-1]（也就是nums[i]!=i+1）的情况，如果有的话这个就是缺失的第一个正数
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # 开始交换位置
        for i in range(n):
            while 1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]:
                j = nums[i]-1
                nums[i], nums[j] = nums[j], nums[i]
        
        # 开始寻找第一个缺失的正数
        for i in range(n):
            if nums[i]!=i+1:
                return i+1

        return n+1 # 没有找到，那么直接返回最大值加上1
        