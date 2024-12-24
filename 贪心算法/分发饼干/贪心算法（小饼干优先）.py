# 方法：贪心（小饼干优先）
# 时间复杂度：
# 1. 分别对g和s数组进行排序，排序的时间复杂度是O(nlogn)，其中n是数组的长度
# 2. 遍历孩子的胃口数组g的时间复杂度是O(m)，其中m是孩子数组的长度
# 整体时间复杂度为O(nlogn+m)，可以简化为O(nlogn)
# 空间复杂度
# 1. 排序操作是就地排序，并没有使用额外的空间
# 整体空间复杂度为O(1)
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # 对饼干和小孩的胃口进行排序
        g.sort()
        s.sort()
        index=0
        for i in range(len(s)): # 遍历饼干
            if index<len(g) and g[index]<=s[i]: # 如果当前孩子的贪心因子小于等于当前饼干的尺寸
                index+=1 # 满足一个孩子，指向下一个孩子
        return index # 返回满足的孩子数量