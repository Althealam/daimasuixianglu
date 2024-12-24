# 方法：贪心（大饼干优先）
# 思路：尽量用大饼干去喂食胃口大的小孩
# 利用局部最优的思想，充分利用饼干尺寸喂饱一个小孩，全局最优就是喂饱尽可能多的小孩
# 分析：贪心策略，先将饼干数组和小孩数组排序。然后从后向前遍历小孩数组，用大饼干优先满足胃口大的，并统计满足小孩的数量
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
        index=len(s)-1 # 饼干数组的下标，从最后一个饼干开始
        result=0 # 记录可以投喂的小孩的数量
        for i in range(len(g)-1,-1,-1): # 遍历胃口，从最后一个孩子开始
            if index>=0 and s[index]>=g[i]: # 遍历饼干（这里index>=0和s[index]>=g[i]的顺序不可以弄反）
                result+=1 # 小孩的数量加1
                index-=1 # 饼干往左边移动一位
        return result

        