class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]
        self.traversal(result, path, candidates, target, 0)
        return result
    
    def traversal(self, result, path, candidates, target, startIndex):
        if sum(path)==target:
            result.append(path[:])
            return 
        if sum(path)>target:
            return
        for i in range(startIndex, len(candidates)):
            path.append(candidates[i])
            self.traversal(result, path, candidates, target, i)
            path.pop()
