class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        path=[]
        self.traversal(result, path, n, k, 1)
        return result
    
    def traversal(self, result, path, n, k, startIndex):
        if len(path)==k and sum(path)==n:
            result.append(path[:])
            return 
        if len(path)>k or sum(path)>n:
            return 
        for i in range(startIndex, 10):
            path.append(i)
            self.traversal(result, path, n, k, i+1)
            path.pop()