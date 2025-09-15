class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        self.traversal(res, path, n, k, 1)
        return res
    
    def traversal(self, result, path, n, k, startIndex):
        if len(path)==k:
            result.append(path[:])
            return 
        for i in range(startIndex, n+1):
            path.append(i)
            self.traversal(result, path, n, k, i+1)
            path.pop()
        