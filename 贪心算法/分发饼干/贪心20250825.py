class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0 # 满足的孩子数量
        for i in range(len(s)): # 遍历饼干尺寸
            if res<len(g) and s[i]>=g[res]:
                res+=1
        return res