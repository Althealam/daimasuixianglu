class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0]) # 按照左边界升序排序
        ans = 0 # 需要移除的区间个数
        for i in range(1, len(intervals)):
            if intervals[i][0]<intervals[i-1][1]:
                ans+=1 # 需要移除的区间个数加上1
                intervals[i][0] = max(intervals[i-1][0], intervals[i][0])
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])
        return ans
        