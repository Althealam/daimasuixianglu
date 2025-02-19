# 思路：
# 1. 按照intervals的第一个元素进行排序
# 2. 如果第二个区间的左值小于第一个区间的右值，则出现了重合，去掉第二个区间，result+=1
# 去掉第二个区间的具体操作为：更新区间的右边界为重合的两个区间的最小右边界

# 时间复杂度：O(nlogn)
# 1. 边界条件判断：O(1)
# 2. 列表排序操作：O(nlogn)
# 3. 遍历列表并判断重叠区间：(n)
# 空间复杂度：O(1)


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals)==0:
            return 0
        result=0 # 记录重叠区间数量
        intervals.sort(key=lambda x: x[0])
        for i in range(0, len(intervals)):
            if i>0 and intervals[i][0]<intervals[i-1][1]: # 存在重叠区间，即右区间的左边界小于左区间的右边界
                result+=1
                # 相当于删除掉一个区间，只保留右边界最小的那个区间
                intervals[i][1]=min(intervals[i][1],intervals[i-1][1])
        return result


        