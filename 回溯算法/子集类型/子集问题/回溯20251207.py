class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.traversal(res, [], nums, 0)
        return res
    
    def traversal(self, res, path, nums, startIndex):
        res.append(path[:])
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.traversal(res, path, nums, i+1)
            path.pop()