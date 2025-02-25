# 本题会超出时间限制
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result=[]
        self.backtracking(result, [], nums, target)
        return len(result)
    
    def backtracking(self, result, path, nums, target):
        if sum(path)==target:
            result.append(path[:])
            return
        for i in range(0, len(nums)):
            if sum(path)>target:
                continue
            path.append(nums[i])
            self.backtracking(result, path, nums, target)
            path.pop()
