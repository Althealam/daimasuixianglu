class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        self.traversal(result, path, nums)
        return result
    
    def traversal(self, result, path, nums):
        if len(path)==len(nums):
            result.append(path[:])
            return 
        for i in range(len(nums)):
            if nums[i] in path:
                continue
            path.append(nums[i])
            self.traversal(result, path, nums)
            path.pop()
        