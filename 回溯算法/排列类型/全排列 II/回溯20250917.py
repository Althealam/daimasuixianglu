class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        nums.sort()
        used = [False]*len(nums)
        self.traversal(result, path, nums, used)
        return result
    
    def traversal(self, result, path, nums, used):
        if len(path)==len(nums) and path not in result:
            result.append(path[:])
            return 
        for i in range(len(nums)):
            if used[i]:
                continue
            if i>0 and nums[i]==nums[i-1] and used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            self.traversal(result, path, nums, used)
            path.pop()
            used[i] = False
        