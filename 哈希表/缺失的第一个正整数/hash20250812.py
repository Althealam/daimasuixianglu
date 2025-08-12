# hash法：用一个set来存储nums中的所有数字，然后从1开始遍历，判断是否在set中，如果不在的话则是smallest_number
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        smallest_number = 1
        while smallest_number in nums_set:
            smallest_number+=1
        return smallest_number
        
        