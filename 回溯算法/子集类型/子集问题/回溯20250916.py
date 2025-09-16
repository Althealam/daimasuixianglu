class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        path = []
        self.traversal(res, path, 0, nums)
        return res
    
    def traversal(self, res, path, startIndex, nums):
        res.append(path[:])
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.traversal(res, path, i+1, nums)
            path.pop()