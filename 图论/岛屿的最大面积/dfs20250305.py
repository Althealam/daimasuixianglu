
# 时间复杂度：O(nxm)
# 1. 输入和网格构建：O(nxm)
# 2. 访问表初始化：O(nxm)
# 3. 遍历网格并进行dfs：O(nxm)
# 4. dfs函数：对于每个单元格最多会尝试4个方向进行探索，每个单元格最多被访问一次 O(nxm)

# 空间复杂度：O(nxm)
# 1. 网格存储：O(nxm)
# 2. 访问表存储：O(nxm)
# 3. 递归调用栈：最坏情况下，当整个网格都是陆地的时候，递归调用栈的深度可以达到O(nxm)

def main():
    n, m=map(int, input().split())

    # 邻接矩阵
    grid=[]
    for i in range(n):
        grid.append(list(map(int, input().split())))
    
    # 访问表
    visited=[[False]*m for _ in range(n)]

    result=0 # 记录最终结果，也就是岛屿的最大面积
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and not visited[i][j]:
                count=1 # count记录目前遍历的陆地的面积
                visited[i][j]=True
                # 调用dfs函数计算当前岛屿面积
                count=dfs(grid, visited, i, j, count)
                # 更新最大岛屿面积
                result=max(count, result)
    print(result)


def dfs(grid, visited, x, y, count):
    """
    深度优先搜索，对一整块陆地进行标记
    """
    # 下、上、左、右
    directions=[[1,0],[-1,0], [0,1], [0,-1]]
    for i, j in directions:
        # 计算下一个位置的坐标
        cur_x=x+i
        cur_y=y+j
        # 判断下标越界
        if cur_x<0 or cur_y<0 or cur_x>=len(grid) or cur_y>=len(grid[0]):
            continue
        # 检查是否为未访问的陆地
        if not visited[cur_x][cur_y] and grid[cur_x][cur_y]==1:
            visited[cur_x][cur_y]=True
            # 递归调用dfs并更新面积
            count=dfs(grid, visited, cur_x, cur_y, count+1)
    return count

if __name__=='__main__':
    main()