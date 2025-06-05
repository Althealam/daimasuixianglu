# 思路：
# 计算总的岛屿数量，总的边数为岛屿数量*4
# 如果有一对相邻的陆地，那么边的总数就要减去2
# 计算相邻岛屿的数量为cover，那么结果=岛屿数量*4-cover*2

# =======读取输入=========
n, m = map(int, input().split())
# n行m列，表示矩阵的行数和列数
grid=[]
for i in range(n):
    grid.append(list(map(int, input().split())))

# =======计算岛屿周长=======
sum_land=0 # 岛屿数量
cover=0 # 统计相邻的岛屿数量
for i in range(n):
    for j in range(m):
        if grid[i][j]==1:
            sum_land+=1
            # 统计上边的相邻岛屿
            if i-1>=0 and grid[i-1][j]==1:
                cover+=1
            # 统计左边的相邻岛屿
            if j-1>=0 and grid[i][j-1]==1:
                cover+=1
result=sum_land*4-cover*2
print(result)
        