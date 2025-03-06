# 时间复杂度：O((nxm)**2)
# 1. 清除与边界相邻的陆地：O((n+m)xnxm)
# （1）遍历边界：O(n+m)
# （2）bfs：O(nxm) 最坏情况下bfs会遍历矩阵中的所有单元格
# 2. 计算孤岛的总面积：O((nxm)**2)
# （1）遍历内部所有单元格：O(nxm)
# （2）bfs：O(nxm)

# 空间复杂度：O(nxm)
# 1. 队列：O(nxm)
# 2. 额外开销：O(1)
from collections import deque

def bfs(grid, x, y):
    """
    用于广度优先搜索一个岛屿，将遍历过的岛屿标记为0，并且返回该岛屿的面积
    """
    area=0
    n, m=len(grid), len(grid[0])
    que=deque([(x, y)]) # 用队列来存储目前遍历的岛屿
    directions=[[1,0], [-1,0], [0,1], [0,-1]]
    while que:
        cur_x, cur_y=que.popleft()
        if cur_x<0 or cur_y<0 or cur_x>=len(grid) or cur_y>=len(grid[0]):
            continue
        if grid[cur_x][cur_y]==0:
            continue
        area+=1
        grid[cur_x][cur_y]=0
        for i, j in directions:
            next_x=cur_x+i
            next_y=cur_y+j
            if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                continue
            que.append((next_x, next_y))
    return area

def main(grid):
    n, m=len(grid), len(grid[0])
    total_area=0 # 记录孤岛的总面积

    # 清除与边界相连接的陆地
    for i in range(n):
        if grid[i][0]==1:
            bfs(grid, i, 0)
        if grid[i][m-1]==1:
            bfs(grid, i, m-1)
    
    for j in range(m):
        if grid[0][j]==1:
            bfs(grid, 0, j)
        if grid[n-1][j]==1:
            bfs(grid, n-1, j)
    
    # 计算孤岛的总面积
    for i in range(1, n-1):
        for j in range(1, m-1):
            if grid[i][j]==1:
                total_area+=bfs(grid, i, j)

    return total_area

n, m=map(int, input().split())

grid=[list(map(int, input().split())) for _ in range(n)]

print(main(grid))