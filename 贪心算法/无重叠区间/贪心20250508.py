# 思路：
# 1. 先按照左边界升序排序
# 2. 从左到右遍历，找到非交叉区间的个数
# 非交叉区间：左区间的右边界大于右区间的左边界
# 更新右区间的右边界
# 3. 用区间总数减去非交叉区间的个数就是要删除的区间个数
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 按照左区间的左边界进行排序
        intervals.sort(key=lambda x: x[0])
        cnt=0 # 交叉的区间个数
        # 遍历区间，判断交叉区间
        for i in range(1, len(intervals)):
            # 找到交叉区间：左区间的右边界大于右区间的左边界
            if intervals[i-1][1]>intervals[i][0]:
                intervals[i][1]=min(intervals[i-1][1], intervals[i][1])
                cnt+=1 # 增加交叉的区间个数
        return cnt
        