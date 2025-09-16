class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        self.traversal(res, path, candidates, target, 0)
        return res
    
    def traversal(self, res, path, candidates, target, startIndex):
        if sum(path)==target:
            res.append(path[:])
            return 
        if sum(path)>target:
            return 
        for i in range(startIndex, len(candidates)):
            if i>startIndex and candidates[i]==candidates[i-1]:
                continue

            path.append(candidates[i])
            self.traversal(res, path, candidates, target, i+1)
            path.pop()
        