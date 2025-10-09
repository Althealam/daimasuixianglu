class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() # greed factor
        s.sort()
        res = 0  
        for i in range(len(s)): # cookie size
            if res<len(g) and s[i]>=g[res]:
                res+=1
        return res