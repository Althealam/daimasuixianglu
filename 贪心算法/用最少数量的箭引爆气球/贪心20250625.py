# 思路：
# 1. 将points按照左边界升序排序
# 2. 遍历points中的气球边界，如果第一个气球的右边界大于等于第二个气球的左边界，则可以使用同一个箭，并且更新第二个气球的边界值
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        points.sort(key=lambda x: x[0]) # 按照x[0]升序排序
        for i in range(1, len(points)):
            if points[i-1][1]>=points[i][0]:
                points[i][0]=max(points[i-1][0], points[i][0])
                points[i][1]=min(points[i-1][1], points[i][1])
            else:
                ans+=1
        return ans