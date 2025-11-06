class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.traversal(s, res, [], 0)
        return res
    
    def traversal(self, s, res, path, startIndex):
        if startIndex==len(s):
            res.append(path[:])
            return
        for i in range(startIndex, len(s)):
            x = s[startIndex:i+1]
            if self.ispalindrom(x):
                path.append(x)
                self.traversal(s, res, path, i+1)
                path.pop()
        
    def ispalindrom(self, s):
        if s==s[::-1]:
            return True
        else:
            return False

        