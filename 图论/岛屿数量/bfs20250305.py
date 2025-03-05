# 思路：
# 输入与初始化：读取网格的行数 n 和列数 m，构建存储陆地和水域信息的二维网格 grid，同时创建相同大小的布尔型访问表 visited 记录各单元格是否被访问过。
# 遍历网格：利用两层循环遍历整个网格，对于每个未访问过的陆地单元格（值为 1），岛屿数量 res 增加 1，并调用 bfs 函数对该陆地及其相连陆地进行广度优先搜索。
# 广度优先搜索：在 bfs 函数中，使用队列 que 存储待探索的单元格坐标，从起始陆地单元格开始，将其加入队列并标记为已访问。之后，不断从队列中取出单元格，向四个方向（上、下、左、右）探索，若新位置未越界且为未访问过的陆地，则将其标记为已访问并加入队列。
# 输出结果：完成网格遍历后，输出统计得到的岛屿数量 res

# 时间复杂度：O(nxm)
# 1. 输入处理与网格构建：O(nxm)
# 2. 访问表初始化：O(nxm)
# 3. 遍历网格并进行bfs：O(nxm)
# 4. bfs函数：借助队列que来实现广度优先搜索，每个单元格最多会被加入队列一次 O(nxm)

# 空间复杂度：O(nxm)
# 1. 网格存储：O(nxm)
# 2. 访问表存储：O(nxm)
# 3. 队列：最坏情况下队列que可能会存储整个网格中的所有陆地单元格 O(nxm)

def main():
    # 处理输入（n行m列）
    n, m=map(int, input().split())

    # 邻接矩阵
    grid=[]
    for i in range(n):
        grid.append(list(map(int, input().split())))
    
    # 访问表
    visited=[[False]*m for _ in range(n)]

    res=0 # 记录岛屿的数量
    for i in range(n):
        for j in range(m):
            # 如果当前节点是陆地并且没有访问过这个节点
            if grid[i][j]==1 and not visited[i][j]:
                res+=1
                bfs(grid, visited, i, j)
    print(res)

from collections import deque
def bfs(grid, visited, x, y):
    directions=[[1,0], [-1,0], [0,1], [0,-1]]
    que=deque([])
    que.append([x,y])
    visited[x][y]=True
    while que:
        cur_x, cur_y=que.popleft()
        for i, j in directions:
            next_x=cur_x+i
            next_y=cur_y+j
            if next_y<0 or next_x<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                visited[next_x][next_y]=True
                que.append([next_x, next_y])



if __name__=='__main__':
    main()

