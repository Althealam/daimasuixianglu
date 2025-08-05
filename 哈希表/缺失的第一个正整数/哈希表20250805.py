# hash法：空间换时间，用一个集合存储数组中的所有正整数，从1开始检查每个正整数是否都在集合中

# 时间复杂度：O(n)
# 空间复杂度：O(n)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            if num>0:
                num_set.add(num)
        smallest_missing = 1
        while smallest_missing in num_set:
            smallest_missing+=1
        return smallest_missing