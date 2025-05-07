# 思路：
# 1. 先按照points的第一个元素进行升序排序
# 2. 遍历points，判断两个相邻的元素：
# （1）第一个元素的右边界超过第二个元素的左边界，则可以使用同一个箭头，更新右边的元素的右边界
# （2）第一个元素的右边接不超过第二个元素的左边界，则不可以使用同一个箭头，需要使用多一个箭头，因此将result+1
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        result=0 # 统计需要使用的箭的数量
        for i in range(1, len(points)):
            if points[i-1][1]>=points[i][0]:
                points[i][1]=min(points[i-1][1], points[i][1])
            else:
                result+=1
        return result+1
        