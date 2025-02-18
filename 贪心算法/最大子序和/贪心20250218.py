# 局部最优：当前连续和为负数的时候就放弃，从下一个元素重复计算连续和，因为负数加上下一个元素连续和只会越来越小
# 全局最优：选取最大连续和

# 思路：遍历nums，从头开始用count累加
# 1. 如果count加上nums[i]变成负数，那么就从nums[i+1]开始从0累加count
# 2. 如果count大于max_count，那么就将max_count变成count

# 时间复杂度：O(n)
# 1. 遍历操作：for遍历nums，nums的长度为n O(n)
# 2. 每次循环的操作：count+=nums[i] 时间复杂度为O(1)

# 空间复杂度：O(1)

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count=float('-inf')
        count=0
        for i in range(len(nums)):
            count+=nums[i]
            if count>max_count:
                max_count=count
            if count<=0: # 如果count<=0，则设置count为0，从下一个i+1开始计算和
                count=0
        return max_count
        

        