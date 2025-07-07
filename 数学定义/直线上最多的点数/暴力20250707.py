# 思路：暴力枚举
# 假设直线一定经过points[i]，那么最多还能经过多少个点
# 在直线一定经过坐标原点的情况下，直线斜率为新坐标和原点连线的斜率。因此只要斜率相同的点，一定在同一条直线上

# 时间复杂度：O(n**2)
# 空间复杂度：O(n)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i, (x, y) in enumerate(points):
            cnt = defaultdict(int) # 计算(x,y)的不同斜率值的点的个数
            for x2, y2 in points[i+1:]:
                dx, dy = x2-x, y2-y
                k = dy/dx if dx else inf
                cnt[k]+=1 # k为斜率值，找到该斜率上有多少个不同的点
                ans = max(ans, cnt[k]) # 这里没有计算(x, y)这个点，最后再加1
        return ans+1
