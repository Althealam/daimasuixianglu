class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        path=[]
        self.traversal(result, path, n, k, 1)
        return result
    def traversal(self, result, path, n, k, startIndex):
        if len(path)==k:
            result.append(path.copy())
            return 
        for i in range(startIndex, n+1):
            path.append(i)
            self.traversal(result, path, n, k, i+1)
            path.pop()