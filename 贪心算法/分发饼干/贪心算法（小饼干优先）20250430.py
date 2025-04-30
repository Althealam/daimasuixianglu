# 贪心策略：把大饼干喂给胃口大的
# 思路：将饼干和胃口排序，然后倒序遍历胃口，判断每个饼干能不能喂给这个胃口，如果不能的话则遍历下一个小孩；如果能的话则将饼干喂給这个小孩，然后饼干往前遍历

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        g是胃口值
        s是饼干尺寸
        """
        g.sort()
        s.sort()
        index=0 # 遍历的胃口索引
        for i in range(len(s)): # 遍历饼干
            if index>=0 and s[i]>=g[index]:
                index+=1
        return index
            