n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

def down_area(grid):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    directions = [[0,1], [0, -1], [1, 0], [-1, 0]]

    def dfs(i, j):
        visited[i][j] = True
        grid[i][j] = 2
        for dx, dy in directions:
            next_x, next_y = i+dx, j+dy
            if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                grid[next_x][next_y] = 2
                visited[next_x][next_y] = True
                dfs(next_x, next_y)
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
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                grid[i][j]=0
            if grid[i][j]==2:
                grid[i][j]=1
    
    return grid

grid = down_area(grid)
for ls in grid:
    print(' '.join(map(str, ls)))