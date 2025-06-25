# 思路：
# 1. 将intervals按照左边界升序排序
# 2. 遍历intervals中的区间，找到交叉区间的个数，并且更新交叉区间的值，将两个交叉的区间合并为一个
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        cnt = 0 # 交叉区间的个数
        for i in range(1, len(intervals)):
            if intervals[i-1][1]>intervals[i][0]: # 交叉区间的值
                cnt+=1
                intervals[i][1]=min(intervals[i-1][1], intervals[i][1])
                intervals[i][0]=max(intervals[i-1][0], intervals[i][0])
        return cnt
    
