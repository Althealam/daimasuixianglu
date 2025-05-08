# 1. 先将区间按照左区间升序排序
# 2. 将第一个区间加入到结果数组res中
# 3. 遍历intervals，判断intervals的第i个区间和res的最后一个区间是否是重叠区间，如果是的话则弹出元素并且更新区间
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        if len(intervals)==1:
            return intervals
        res=[intervals[0]] # 统计合并区间后的区间值
        for i in range(1, len(intervals)):
            if res[-1][1]>=intervals[i][0]:
                intervals[i][1]=max(res[-1][1], intervals[i][1])
                intervals[i][0]=min(res[-1][0], intervals[i][0])
                res.pop()
            res.append(intervals[i])
        return res

