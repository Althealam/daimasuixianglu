class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.traversal(res, k, n, [], 1)
        return res
    
    def traversal(self, res, k, n, path, startIndex):
        if sum(path[:])==n and len(path[:])==k:
            res.append(path[:])
            return 
        for i in range(startIndex, 10):
            path.append(i)
            self.traversal(res, k, n, path, i+1)
            path.pop()