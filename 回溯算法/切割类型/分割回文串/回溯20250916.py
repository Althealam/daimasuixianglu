class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        self.traversal(res, path, 0, s)
        return res
    
    def traversal(self, res, path, startIndex, s):
        if startIndex==len(s):
            res.append(path[:])
            return
        for i in range(startIndex, len(s)):
            x = s[startIndex:i+1]
            if self.ishuiwen(x):
                path.append(x)
                self.traversal(res, path, i+1, s)
                path.pop()
    
    def ishuiwen(self, x):
        if x==x[::-1]:
            return True
        return False
        