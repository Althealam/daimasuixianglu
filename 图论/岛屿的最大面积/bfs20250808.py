import collections
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))


def max_area(grid):
    visited = [[False]*len(grid[0]) for _ in range(n)]

    max_area = 0
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def bfs(i, j):
        current_area=1
        visited[i][j]=True
        queue = collections.deque([])
        queue.append([i, j])
        while queue:
            cur_x, cur_y = queue.popleft()
            for dx, dy in directions:
                next_x, next_y = cur_x+dx, cur_y+dy
                if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                    continue
                if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                    visited[next_x][next_y] = True
                    current_area+=bfs(next_x, next_y)
        return current_area
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and grid[i][j]==1:
                current_area = bfs(i, j)
                max_area = max(max_area, current_area)
    return max_area

max_area = max_area(grid)
print(max_area)