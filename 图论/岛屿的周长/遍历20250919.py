n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

sum_land = 0 # 岛屿的周长
cover = 0 # 覆盖的数量
for i in range(n):
    for j in range(m):
        if grid[i][j]==1:
            sum_land+=1
            if i-1>=0 and grid[i-1][j]==1:
                cover+=1
            if j-1>=0 and grid[i][j-1]:
                cover+=1
res = sum_land*4-cover*2
print(res)