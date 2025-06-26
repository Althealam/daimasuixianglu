# 思路：
# 1. 将区间按照左边升序排序
# 2. 将第一个区间放入到res中
# 3. 遍历intervals剩下的区间，判断当前遍历的区间的左边界和res最后一个区间的右边界，如果重合的话则弹出res中的最后一个区间，更新区间的值并加入
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1]>=intervals[i][0]:
                intervals[i][0]=min(intervals[i][0], res[-1][0])
                intervals[i][1]=max(intervals[i][1], res[-1][1])
                res.pop()
            res.append(intervals[i])
        return res