class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()
        self.traversal(result, path, candidates, target, 0)
        return result
    
    def traversal(self, result, path, candidates, target, startIndex):
        if sum(path)==target:
            result.append(path[:])
            return 
        if sum(path)>target:
            return 
        for i in range(startIndex, len(candidates)):
            if i>startIndex and candidates[i]==candidates[i-1]:
                continue
            path.append(candidates[i])
            self.traversal(result, path, candidates, target, i+1)
            path.pop()

