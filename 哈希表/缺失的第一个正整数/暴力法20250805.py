# 暴力法：对数组排序，遍历排序后的数组，找到第一个不满足nums[i]==i+1的位置；如果所有位置都满足，那么返回n+1

# 时间复杂度：O(nlogn)
# 空间复杂度：O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        smallest_missing = 1
        for num in nums:
            if num==smallest_missing:
                smallest_missing+=1
            elif num>smallest_missing:
                break
        return smallest_missing
