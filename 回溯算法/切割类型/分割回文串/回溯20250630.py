class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        self.traversal(result, path, 0, s)
        return result
    
    def traversal(self, result, path, startIndex, s):
        if startIndex==len(s):
            result.append(path[:])
            return 
        for i in range(startIndex, len(s)):
            x = s[startIndex:i+1]
            if self.ishuiwei(x):
                path.append(x)
                self.traversal(result, path, i+1, s)
                path.pop()
    
    def ishuiwei(self, x):
        if x==x[::-1]:
            return True
        return False