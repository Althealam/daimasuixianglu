n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

def island_area(grid):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]

    directions =[[0, 1], [0, -1], [1, 0], [-1, 0]]

    def dfs(i, j):
        visited[i][j] = True
        grid[i][j] = 2
        for dx, dy in directions:
            next_x, next_y = dx+i, dy+j
            if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                visited[next_x][next_y] = True
                grid[next_x][next_y] = 2
                dfs(next_x, next_y)

    # 处理上下左右四个边界
    for i in range(len(grid)):
        if not visited[i][0] and grid[i][0]==1:
            dfs(i, 0)
        if not visited[i][len(grid[0])-1] and grid[i][len(grid[0])-1]==1:
            dfs(i, len(grid[0])-1)
    
    for j in range(len(grid[0])):
        if not visited[0][j] and grid[0][j]==1:
            dfs(0, j)
        if not visited[len(grid)-1][j] and grid[len(grid)-1][j]==1:
            dfs(len(grid)-1, j)

    area_grid = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                area_grid+=1
    return area_grid

area_grid = island_area(grid)
print(area_grid)
