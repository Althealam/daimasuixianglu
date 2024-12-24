# 思路：判断重叠区间，并且判断两个区间重叠后需要进行合并操作

# 时间复杂度：
# 1. 排序：O(nlogn)
# 2. 遍历区间合并：O(n)
# 总的时间复杂度为O(nlogn)
# 空间复杂度：
# 1. result用来存储合并后的区间：O(n)
# 2. 排序：原地进行，因此为O(1)
# 总的空间复杂度为O(1)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 定义二维数组，用来存放合并后的区间结果
        result=[]
        
        # 区间集合为空直接返回
        if len(intervals)==0:
            return result

        # 对左边界进行排序，使得相邻的区间放在一起
        intervals.sort(key=lambda x: x[0]) 
        # 先放进去一个区间
        result.append(intervals[0])
        
        for i in range(1,len(intervals)):
            if intervals[i][0]<=result[-1][1]: # 区间重叠
                # 合并区间
                # result[-1][1]表示的是倒数最后一个区间的右边界
                result[-1][1]=max(result[-1][1],intervals[i][1]) # 修改合并区间的右边界
                result[-1][0]=min(result[-1][0],intervals[i][0]) # 修改合并区间的左边界
            else: # 区间不重叠
                result.append(intervals[i])
        return result

solution=Solution()
intervals= [[1,3],[2,6],[8,10],[15,18]]   
result=solution.merge(intervals)
      
                
        