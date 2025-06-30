class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        path = []
        self.traversal(result, path, s, 0)
        return result
    
    def traversal(self, result, path, s, startIndex):
        if startIndex==len(s) and len(path)==4:
            result.append('.'.join(path[:]))
            return
        for i in range(startIndex, len(s)):
            x = s[startIndex:i+1]
            if self.isvalid(x):
                path.append(x)
                self.traversal(result, path, s, i+1)
                path.pop()
    
    def isvalid(self, x):
        if len(x)>1:
            if int(x[0])==0:
                return False
            if int(x)>255 or int(x)<0:
                return False
        elif len(x)==1:
            if int(x)==0:
                return True
        return True