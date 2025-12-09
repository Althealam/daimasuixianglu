class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            if intervals[i-1][1]>intervals[i][0]:
                ans+=1
                intervals[i][0] = max(intervals[i-1][0], intervals[i][0])
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])
        return ans