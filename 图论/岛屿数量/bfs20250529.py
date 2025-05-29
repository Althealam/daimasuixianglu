from collections import deque
# 使用队列来模拟bfs
def bfs(grid, visited, i, j):
    directions=[[0, 1], [0, -1], [1, 0], [-1, 0]]
    que=deque([])
    que.append([i, j])
    visited[i][j]=True
    while que:
        cur_x, cur_y=que.popleft()
        for i, j in directions:
            next_x=cur_x+i
            next_y=cur_y+j
            if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                visited[next_x][next_y]=1
                que.append([next_x, next_y])



n, m=map(int, input().split())
grid=[]
for i in range(n):
    grid.append(list(map(int, input().split())))
res=0
visited=[[False]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j] and grid[i][j]==1:
            res+=1
            bfs(grid, visited, i, j)
print(res)
