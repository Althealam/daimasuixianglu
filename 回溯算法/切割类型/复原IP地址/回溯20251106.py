class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.traversal(s, 0, res, [])
        return res
    
    def traversal(self, s, startIndex, res, path):
        if startIndex==len(s) and len(path)==4:
            res.append('.'.join(path[:]))
            return 
        for i in range(startIndex, len(s)):
            if self.isvalid(s[startIndex:i+1]):
                path.append(s[startIndex:i+1])
                self.traversal(s, i+1, res, path)
                path.pop()
    
    def isvalid(self, x):
        if int(x)<0 or int(x)>255:
            return False
        if int(x)!=0 and int(x[0])==0:
            return False
        if int(x)==0 and len(x)>1:
            return False
        return True
        