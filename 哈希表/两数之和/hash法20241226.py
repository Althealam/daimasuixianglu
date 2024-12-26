# 使用哈希法的情况：查询一个元素是否出现过、一个元素是否在集合里面
# 分析：用一个hash来记录nums中每个元素，如果出现过则记录为对应的下表
# 对于每个元素nums[i]，判断target-nums[i]是否在hash表中出现过，如果没有的话则继续遍历下一个元素
# 时间复杂度：O(n)（遍历元素）
# 空间复杂度：O(n)（字典）

# 注意：本题有一个问题就是，如果数组[3,3]，target=3，这时候怎么处理hash表，因为hash表在这时候没办法使用数组（长度无法确定），因此我们没办法去统计每个元素出现的长度。那么这时候，我们可以通过边遍历（记录数组出现的元素）边判断是否达到了条件，这样可以避免这种情况的发生

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
        