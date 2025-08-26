class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1 # 需要的箭数量
        points.sort(key=lambda x: x[0]) # 按照左边界升序排序
        for i in range(1, len(points)):
            if points[i-1][1]>=points[i][0]:
                points[i][1] = min(points[i-1][1], points[i][1])
                points[i][0] = max(points[i-1][0], points[i][0])
            else:
                ans+=1
        return ans

        