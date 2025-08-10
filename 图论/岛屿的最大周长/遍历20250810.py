n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

max_land_perimeter = 0 # 岛屿的最大周长
current_land_perimeter = 0 # 当前岛屿的周长
directions = [[1, 0], [0, 1], [-1, 0]], [0, -1]

def dfs(i, j, grid):
    for dx, dy in directions:
        next_x, next_y = i+dx, j+dy
        if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
            continue
        if 


for i in range(n):
    for j in range(m):
        if grid[i][j]==1: # 当前遍历的是岛屿
