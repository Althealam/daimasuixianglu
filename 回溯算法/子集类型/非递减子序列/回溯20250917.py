class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        self.traversal(result, path, 0, nums)
        return result
    
    def traversal(self, result, path, startIndex, nums):
        if len(path)>=2 and path not in result:
            result.append(path[:])
        for i in range(startIndex, len(nums)):
            if path and nums[i]<path[-1]:
                continue
            path.append(nums[i])
            self.traversal(result, path, i+1, nums)
            path.pop()
        