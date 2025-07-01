class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        nums.sort()
        self.traversal(result, path, 0, nums)
        return result
    
    def traversal(self, result, path, startIndex, nums):
        result.append(path[:])
        for i in range(startIndex, len(nums)):
            if i>startIndex and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            self.traversal(result, path, i+1, nums)
            path.pop()
        