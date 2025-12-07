class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.traversal(n, k, res, [], 1)
        return res
    
    def traversal(self, n, k, res, path, startIndex):
        if len(path[:])==k:
            res.append(path[:])
            return 
        for i in range(startIndex, n+1):
            path.append(i)
            self.traversal(n, k, res, path, i+1)
            path.pop()