# 局部最优：当气球出现重叠，一起射
# 全局最优：把所有气球射爆所用的弓箭最少

# 思路：判断气球A和气球B是否重叠
# 1. 如果气球A的边界xend>气球B的边界x的边界xstart，则是重叠的
# 2. 对于重叠的气球，更新其最小的重叠边界xend=min(point[i][1], points[i+1][1])
# 3. 如果遇到了不重叠的气球，则将result+=1

# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points)==0: # 如果没有气球，则直接返回0
            return 0
        points.sort(key=lambda x: x[0]) # 按照xstart进行排序
        result=0 # 所需要的弓箭数
        for i in range(0, len(points)):
            if i>0 and points[i-1][1]>=points[i][0]: # 注意，如果两个气球的xstart和xend是重叠的，也可以共用一只弓箭
                points[i][1]=min(points[i-1][1],points[i][1]) # 更新重叠的气球边界
            else:
                result+=1

        return result


        