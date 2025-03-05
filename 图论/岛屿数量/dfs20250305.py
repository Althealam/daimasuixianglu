# 思路：
# 输入处理：读取网格的行数 n 和列数 m，并构建二维网格 grid 存储陆地和水域信息，同时创建一个同样大小的 visited 数组用于记录每个单元格是否被访问过。
# 遍历网格：通过两层循环遍历整个网格，对于每个未访问过的陆地单元格（值为 1），岛屿数量 res 加 1，并调用 dfs 函数对该陆地及其相连的陆地进行深度优先搜索。
# 深度优先搜索：在 dfs 函数中，从当前陆地单元格出发，尝试向四个方向（下、右、上、左）探索，若新位置未越界且为未访问过的陆地，则标记为已访问并继续递归搜索。
# 输出结果：遍历结束后，输出统计得到的岛屿数量 res。

# 时间复杂度：O(nxm)
# 1. 输入处理和网格初始化：O(nxm)
# 2. 访问表初始化：O(nxm)
# 3. 遍历网格并进行dfs：O(nxm)
# 4. dfs函数：对于每个单元格最多会向4个方向进行尝试，并且每次访问时的操作事假为O(1) O(nxm)

# 空间复杂度：O(nxm)
# 1. 网格存储：O(nxm)
# 2. 访问表存储：O(nxm)
# 3. 递归调用栈：O(nxm) DFS的深度可能达到nxm，比如当整个网格都是陆地时
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
                visited[i][j]=True
                dfs(grid, visited, i, j)
    print(res)

def dfs(grid, visited, x, y):
    """
    对一块陆地进行深度优先遍历并标记
    遇到一个没有遍历过的节点陆地，计数器就加1，并且把该节点陆地所能遍历到的陆地都标记上
    """
    direction=[[0,1], [1,0], [0,-1], [-1,0]] # 四个方向：下、右、上、左
    for i, j in direction:
        next_x=x+i
        next_y=y+j
        # 下标越界，跳过(x是行，y是列)
        # 需要确保x和y都在行列的范围内
        if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
            continue
        # 未访问过，并且next_x和next_y是陆地，那么则标记为访问过
        if not visited[next_x][next_y] and grid[next_x][next_y]==1:
            visited[next_x][next_y]=True
            dfs(grid, visited, next_x, next_y)
    
if __name__=='__main__':
    main()

