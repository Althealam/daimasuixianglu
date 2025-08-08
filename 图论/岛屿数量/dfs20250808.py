n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

def island_count(grid):
    visited = [[False]*len(grid[0]) for _ in range(len(grid))]
    directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
    
    def dfs(i, j):
        for dx, dy in directions:
            next_x = dx+i
            next_y = dy+j
            if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                visited[next_x][next_y] = True
                dfs(next_x, next_y)
        

    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and grid[i][j]==1:
                cnt+=1
                visited[i][j] = True
                dfs(i, j)
    return cnt

res = island_count(grid)
print(res)
