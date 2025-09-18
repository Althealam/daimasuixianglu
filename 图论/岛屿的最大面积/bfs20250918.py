import collections
n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [[False]*m for _ in range(n)]
max_area = float('-inf')
directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(i, j):
    visited[i][j] = True
    current_area = 1
    queue = collections.deque()
    queue.append([i, j])
    while queue:
        cur_x, cur_y = queue.popleft()
        for dx, dy in directions:
            next_x, next_y = cur_x+dx, cur_y+dy
            if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                visited[next_x][next_y]=True
                current_area+=bfs(next_x, next_y)
    return current_area

for i in range(n):
    for j in range(m):
        if grid[i][j]==1 and not visited[i][j]:
            current_area = bfs(i, j)
            max_area = max(max_area, current_area)

print(max_area if max_area!=float('-inf') else 0)