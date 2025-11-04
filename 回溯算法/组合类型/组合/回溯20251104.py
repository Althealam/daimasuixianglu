class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.traversal(res, [], n, k, 1)
        return res
    
    def traversal(self, res, path, n, k, startIndex):
        if len(path)==k:
            res.append(path[:])
            return 
        for i in range(startIndex, n+1):
            path.append(i)
            self.traversal(res, path, n, k, i+1)
            path.pop()