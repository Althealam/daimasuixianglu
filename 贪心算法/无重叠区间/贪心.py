# 分析：相当于重叠了多少区间，计算这些重叠的区间的数量，输出即可
# 参考用最少数量的弓箭射气球的题目，思路是类似的
# 1. 不重叠：i的左边界>=i-1的右边界
# 2. 重叠：i的左边界<i-1的右边界 重叠的时候，count+=1
# 更新i的右边界，判断是否也要删除另外一个区间

# 时间复杂度：
# 1. 排序：O(nlogn)
# 2. 遍历：O(n)
# 总的时间复杂度为O(nlogn)
# 空间复杂度：
# 1. 排序操作是原地进行的，O(1)
# 2. 其他使用的额外空间是常数级别的
# 总的空间复杂度为O(1)
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        count=0 # 记录重叠了多少区间
        intervals.sort(key=lambda x: x[0]) # 按照左边界排序
        for i in range(1,len(intervals)):
            if intervals[i][0]<intervals[i-1][1]:
                count+=1
                intervals[i][1]=min(intervals[i][1],intervals[i-1][1])
        return count
            

        