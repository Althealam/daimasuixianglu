# 时间复杂度：O(mn)
# 1. 输入读取部分：O(mn)
# 2. 网格遍历部分：O(mn)
# 3. 其他操作：O(1)

# 空间复杂度：O(mn)
# 1. 存储网格睡觉：O(mn)
# 2. 其他变量：O(1)

# 思路：假设每个陆地单元格都独立存在，那么每个单元格的周长都是4.然后考虑相邻的单元格，每有一对相邻的陆地单元格，就有2条边会重复。因此如果有n个单元格相邻，那么就会有2*n条边重复。

def main():
    n, m=map(int, input().split())

    grid=[]
    for i in range(n):
        grid.append(list(map(int, input().split())))


    # 陆地数量
    sum_land=0
    # 相邻数量
    cover=0

    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                sum_land+=1
                # 统计上边的相邻陆地
                if i>0 and grid[i-1][j]==1:
                    cover+=1
                # 统计左边的相邻陆地
                if j>0 and grid[i][j-1]==1:
                    cover+=1
                # 不需要统计下边和右边的陆地，避免重复运算
    
    result=sum_land*4-cover*2
    print(result)

if __name__=='__main__':
    main()