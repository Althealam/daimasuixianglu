class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        self.traversal(res, path, candidates, target, 0)
        return res
    
    def traversal(self, res, path, candidates, target, startIndex):
        if sum(path)==target:
            res.append(path[:])
            return 
        if sum(path)>target:
            return 
        for i in range(startIndex, len(candidates)):
            path.append(candidates[i])
            self.traversal(res, path, candidates, target, i)
            path.pop()
        