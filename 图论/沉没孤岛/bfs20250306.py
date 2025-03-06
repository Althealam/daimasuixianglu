# 时间复杂度：O((n+m)xnxm)
# 1. 从边界进行bfs标记与边界相连的陆地：O((n+m)xnxm)
# （1）遍历边界：O(n+m)
# （2）dfs操作：O(nxm) 
# 2. 处理 grid矩阵：O(nxm)
# 3. 打印结果：O(nxm)

# 空间复杂度：O(nxm)
# 1. 递归调用栈的深度：O(nxm)
# 2. 其他额外空间：O(1)
# 3. grid矩阵：O(nxm)

# 思路：把和边界相连的岛屿记录为2，剩下的就是孤岛。然后最后将孤岛变成0,2边成1即可

from collections import deque
def bfs(grid, x, y):
    """
    使用广度优先搜索标记与边界相连的矩阵
    :param grid：岛屿矩阵
    :param x: 起始单元格的行索引
    :param y: 起始单元格的列索引
    """
    que=deque([(x,y)]) 
    grid[x][y]=2
    directions=[[1,0], [-1,0], [0,1], [0,-1]]
    while que:
        cur_x, cur_y=que.popleft()
        for i,j in directions:
            next_x=cur_x+i
            next_y=cur_y+j
            if next_x<0 or next_y<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                continue
            if grid[next_x][next_y]==2 or grid[next_x][next_y]==0:
                continue
            grid[next_x][next_y]=2
            que.append((next_x, next_y))


def main():
    n, m=map(int, input().split())
    grid=[list(map(int, input().split())) for _ in range(n)]

    # 从左侧边和右侧边，向中间遍历
    # 将左侧边和右侧边的相连陆地标记为2
    for i in range(n):
        if grid[i][0]==1:
            bfs(grid, i, 0)
        if grid[i][m-1]==1:
            bfs(grid, i, m-1)
    
    # 从上边和下边，向中间遍历
    # 将上边和下边的相连陆地标记为2
    for j in range(m):
        if grid[0][j]==1:
            bfs(grid, 0, j)
        if grid[n-1][j]==1:
            bfs(grid, n-1, j)
        
    # 处理grid矩阵
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                grid[i][j]=0
            if grid[i][j]==2:
                grid[i][j]=1
    
    # 打印结果
    for row in grid:
        print(' '.join(map(str, row)))

if __name__=='__main__':
    main()