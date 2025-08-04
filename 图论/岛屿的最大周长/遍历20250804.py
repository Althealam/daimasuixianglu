def max_island_perimeter(grid):
    if not grid or not grid[0]:
        return 0
    n, m = len(grid), len(grid[0])
    max_perimeter = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                perimeter = 4

                # 检查上方单元格
                if i>0 and grid[i-1][j]==1:
                    perimeter-=1
                # 检查下方单元格
                if i<n-1 and grid[i+1][j]==1:
                    perimeter-=1
                # 检查左边单元格
                if j>0 and grid[i][j-1]==1:
                # 检查右边单元格
                    perimeter-=1
                if j<m-1 and grid[i][j+1]==1:
                    perimeter-=1

                # 更新最大周长
                max_perimeter = max(max_perimeter, perimeter)
    return max_perimeter

grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]
res = max_island_perimeter(grid)
print(res)