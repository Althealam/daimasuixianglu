n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
sum_land = 0 # 岛屿周长
cover = 0 # 覆盖的数量
# 覆盖的数量加1时，则岛屿的周长减去2
for i in range(n):
    for j in range(m):
        if grid[i][j]==1:
            # 统计上边的陆地
            sum_land+=1
            if i-1>=0 and grid[i-1][j]==1:
                cover+=1
            if j-1>=0 and grid[i][j-1]==1:
                cover+=1
result = sum_land*4-cover*2
print(result)