# 时间复杂度：O((nxm)**2)
# 1. 清除与边界相连的陆地：最坏的情况下矩阵边界上的每个单元格都为陆地，即O(n+m)
# 每次调用dfs函数，都会递归遍历到矩阵的所有单元格，因此是O((n+m)xnxm)
# 2. 计算孤岛面积：通过两层循环遍历矩阵内部的单元格 O((nxm)**2)

# 空间复杂度：O(nxm)
# 1. 递归调用栈的空间：dfs进行深度优先搜索，递归调用栈的深度取决于矩阵中最大的连通趋于的大小，最坏情况下为O(nxm)
# 2. 额外空间：O(1)
# 3. 邻接矩阵：O(nxm)

# 思路：
# 1. 清除与矩阵边界相连的陆地，这样剩下的陆地部分就只包含孤岛和不完整的岛屿碎片
# 2. 遍历矩阵内部（非边界）的陆地单元格，对于每个未被访问过的陆地，使用dfs算法计算器所在孤岛的面积，并将所有孤岛的面积累加起来得到总面积


def dfs(grid, x, y):
    """
    用于深度优先搜索一个岛屿，将遍历过的陆地标记为0，并返回该岛屿的面积
    """
    area = 1 # 该岛屿的面积
    grid[x][y] = 0 # 记录该位置已访问过
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        # 如果该位置越界则跳过
        if new_x<0 or new_y<0 or new_x>=len(grid) or new_y>=len(grid[0]):
            continue
        # 如果该位置已访问过则跳过
        if grid[new_x][new_y]==0:
            continue
        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == 1:
            area += dfs(grid, new_x, new_y)
    return area


def main(grid):
    n, m = len(grid), len(grid[0])
    total_area = 0 # 记录孤岛的总面积
    
    # 先清除与边界相连的陆地（也就是整个岛屿的四面）
    for i in range(n):
        if grid[i][0] == 1:
            dfs(grid, i, 0)
        if grid[i][m - 1] == 1:
            dfs(grid, i, m - 1)
    for j in range(m):
        if grid[0][j] == 1:
            dfs(grid, 0, j)
        if grid[n - 1][j] == 1:
            dfs(grid, n - 1, j)
    
    # 计算孤岛面积（不遍历边界）
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] == 1:
                total_area += dfs(grid, i, j)
    return total_area


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
print(main(grid))
