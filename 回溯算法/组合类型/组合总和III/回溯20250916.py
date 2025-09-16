class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        self.traversal(res, path, 1, k, n)
        return res

    def traversal(self, res, path, startIndex, k, n):
        if len(path)==k and sum(path)==n:
            res.append(path[:])
            return 
        for i in range(startIndex, 10):
            path.append(i)
            self.traversal(res, path, i+1, k, n)
            path.pop()
        