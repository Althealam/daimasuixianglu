from collections import deque
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

def max_island_perimeter(grid):
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def bfs(i, j):
        q = deque()
        q.append([i, j])
        visited[i][j] = True
        perimeter = 0
        while q:
            cur_i, cur_j = q.popleft()
            per+=4 # 每个陆地格子初始贡献为4
            for di, dj in directions:
                next_x, next_y = cur_i+di, cur_j+dj
                if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                    continue
                if grid[next_x][next_y]==1:
                    perimeter-=1
                    if not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        q.append([next_x, next_y])
        return perimeter

    max_per = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==1 and not visited[i][j]:
                current_per = bfs(i, j)
                if current_per>max_per:
                    max_per = current_per
    return max_per

max_per = max_island_perimeter(grid)
print(max_per)
