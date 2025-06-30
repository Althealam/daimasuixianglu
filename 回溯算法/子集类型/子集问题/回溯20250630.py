class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        self.traversal(result, path, nums, 0)
        return result
    
    def traversal(self, result, path, nums, startIndex):
        result.append(path[:])
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.traversal(result, path, nums, i+1)
            path.pop()
        