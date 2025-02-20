# 思路：
# 1. 将intervals按照intervals[i][0]进行排序
# 2. 直接将第一个区间放进去
# 3. 从1到len(intervals)-1遍历区间，判断当前遍历的区间和结果集的最后一个区间的右边界是否有重复，有的话则更新结果集的最后一个区间的右边界
# 4. 如果没有重合的话，则直接加入区间即可

# 时间复杂度：O(nlogn）
# 1. 排序操作：O(nlogn)
# 2. 遍历合并操作：O(n)
# 空间复杂度：O(n）
# 1. result存储结果集，O(n)
# 2. 排序操作的额外空间：O(n)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0]) # 按照左边界进行排序
        result=[] # 结果集
        
        result.append(intervals[0]) # 第一个区间直接放进去
        for i in range(1, len(intervals)):
            if result[-1][1]>=intervals[i][0]: # 重叠区间
                result[-1][1]=max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i]) # 区间不重叠
        
        return result