class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False]*n for _ in range(m)]
                
        def dfs(i, j):
            current_area=1
            visited[i][j]=True
            for dx, dy in directions:
                next_x = i+dx
                next_y = j+dy
                if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                    continue
                if 0<=next_x<m and 0<=next_y<n and not visited[next_x][next_y] and grid[next_x][next_y]==1:
                    visited[next_x][next_y] = True
                    current_area+=dfs(next_x, next_y)
            return current_area
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]==1:
                    current_area = dfs(i, j)
                    max_area = max(max_area, current_area)
        return max_area


        
        