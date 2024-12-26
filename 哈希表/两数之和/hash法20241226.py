# 使用哈希法的情况：查询一个元素是否出现过、一个元素是否在集合里面
# 分析：首先用一个hash来记录nums中每个元素，如果出现过则记为1
# 对于每个元素nums[i]，判断target-nums[i]是否在hash表中出现过，如果没有的话则继续遍历下一个元素
# 时间复杂度：O(n)（遍历元素）
# 空间复杂度：O(n)（字典）
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        records=dict()
        for i in range(len(nums)):
            if target-nums[i] in records:
                return [records[target-nums[i]],i]
            records[nums[i]]=i
        return []
        