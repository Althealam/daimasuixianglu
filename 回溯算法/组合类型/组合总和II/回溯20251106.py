class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.traversal(candidates, target, res, [], 0)
        return res
    
    def traversal(self, candidates, target, res, path, startIndex):
        if sum(path[:])==target:
            res.append(path[:])
            return 
        if sum(path[:])>target:
            return
        for i in range(startIndex, len(candidates)):
            if i>startIndex and candidates[i]==candidates[i-1]:
                continue
            path.append(candidates[i])
            self.traversal(candidates, target, res, path, i+1)
            path.pop()
        