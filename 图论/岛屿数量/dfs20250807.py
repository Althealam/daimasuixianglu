class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False]*len(grid[0]) for _ in range(len(grid))]
        def dfs(x, y, grid, visited):
            for dx, dy in directions:
                next_x = x+dx
                next_y = y+dy
                if 0<=next_x<len(grid) and 0<=next_y<len(grid[0]) and not visited[next_x][next_y] and grid[next_x][next_y]=='1':
                    visited[next_x][next_y] = True
                    dfs(next_x, next_y, grid, visited)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]=='1':
                    cnt+=1
                    visited[i][j]=True
                    dfs(i, j, grid, visited)
        
        return cnt