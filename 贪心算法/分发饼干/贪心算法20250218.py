# 时间复杂度：
# 1. 排序操作：O(nlogn)和O(mlogm)，其中n是饼干的数量，m是小孩的数量
# 2. 遍历操作：for循环遍历孩子的贪心因子列表g，时间复杂度为O(1)，循环会执行m次，遍历操作的时间复杂度为O(m)

# 空间复杂度：O(1)
# 1. 额外空间使用：index、result O(1)
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort() # 将孩子的贪心因子排序
        s.sort() # 将帮干的尺寸排序
        index=len(s)-1 # 从饼干的最后一个开始
        result=0 # 满足孩子的数量
        for i in range(len(g)-1, -1, -1): # 遍历孩子
            if index>=0 and s[index]>=g[i]:
                result+=1
                index-=1 # 遍历饼干
        return result