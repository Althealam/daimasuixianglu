class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()
        self.traversal(res, path, 0, nums)
        return res
    
    def traversal(self, res, path, startIndex, nums):
        res.append(path[:])
        for i in range(startIndex, len(nums)):
            if i>startIndex and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            self.traversal(res, path, i+1, nums)
            path.pop()
        