class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        self.traversal(result, path, 0, nums)
        return result
    
    def traversal(self, result, path, startIndex, nums):
        if len(path)>=2 and path[:] not in result:
            result.append(path[:])

        for i in range(startIndex, len(nums)):
            if i>startIndex and nums[i]==nums[i-1]:
                continue
            
            if len(path)!=0 and nums[i]>=path[-1]:
                path.append(nums[i])
            elif len(path)==0:
                path.append(nums[i])
            self.traversal(result, path, i+1, nums)
            if len(path)!=0:
                path.pop()
        