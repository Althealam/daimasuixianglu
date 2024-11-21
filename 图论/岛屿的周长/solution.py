# 1. 遍历每一个空格，遇到岛屿则计算其上下左右的空格情况
# 如果该陆地上下左右的空格是有水域，则说明是一条边
# 2. 陆地的右边空格是水域，则说明找到一条边
# 3. 如果该陆地上下左右的空格出界了，则说明是一条边

def main():
    import sys
    input=sys.stdin.read
    data=input().split()
    
    # 读取n和m
    n=int(data[0])
    m=int(data[1])
    
    # 初始化grid
    grid=[]
    index=2
    for i in range(n):
        grid.append([int(data[index+j]) for j in range(m)])
        index+=m
    
    sum_land=0 # 陆地数量
    cover=0 # 相邻数量
    
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                sum_land+=1
                # 统计上边相邻陆地
                if i-1>=0 and grid[i-1][j]==1:
                    cover+=1
                # 统计左边相邻陆地
                if j-1>=0 and grid[i][j-1]==1:
                    cover+=1
    result=sum_land*4-cover*2
    print(result)

if __name__=='__main__':
    main()