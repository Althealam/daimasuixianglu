# 注意：本题目要求解的是不和走廊相连接的最大主题面积，因此需要ans = max(ans, current_ans)
class Solution:
    def largestArea(self, grid: List[str]) -> int:
        grid = [list(s) for s in grid]

        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        ans = 0
        def dfs(i, j, k):
            """求解不和0以及走量相连接的主题空间面积"""
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0':
                return -inf
            if grid[i][j]!=k:
                return 0
            grid[i][j] = '7'
            return 1+dfs(i+1, j, k)+dfs(i-1, j, k)+dfs(i, j-1, k)+dfs(i, j+1, k)
        for i in range(m):
            for j in range(n):
                if grid[i][j]!='0' and grid[i][j]!='7': # 不为7和不为0的单元格
                    ans = max(ans, dfs(i, j, grid[i][j]))
        return ans
