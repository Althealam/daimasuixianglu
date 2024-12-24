direction=[[0,1],[1,0],[0,-1],[-1,0]]
# [0,1]表示向右移动
# [1,0]表示向下移动
# [0,-1]表示向左移动
# [-1,0]表示向上移动
# 这些方向用于在二维网格中寻找相邻格子

# 时间复杂度

def dfs(grid,visited,x,y):
    """
    对一块陆地进行深度优先遍历，并标记（本段代码相当于是找[x,y]的岛屿，并且标记好岛屿）
    grid：二维网络，通常由0和1组成，1表示陆地，0表示水域
    visited：二维布尔数组，用于记录是否访问过某个格子
    x,y：当前正在访问的格子的数量
    """
    for i,j in direction:
        # 从当前格子(x,y)开始，递归的遍历与之相邻的陆地格子，并将其标记为已访问
        # 遍历direction的每个方向，计算当前格子移动到下一个格子的坐标(next_x,next_y)中
        next_x=x+i
        next_y=y+j
        # 下标越界，跳过
        if next_x<0 or next_x>=len(grid) or next_y<0 or next_y>=len(grid[0]):
            continue
        # 未访问的陆地，标记并调用深度优先搜索
        if not visited[next_x][next_y] and grid[next_x][next_y]==1:
            visited[next_x][next_y]=True
            dfs(grid,visited,next_x,next_y)

def main(): 
    # 对输入进行处理，n和m分别表示矩阵的行和列
    # 矩阵的元素分别为1或者0
    n,m=map(int,input().split())
    
    # 邻接矩阵
    grid=[]
    for i in range(n): # 读取岛屿矩阵
        grid.append(list(map(int,input().split())))
        
    # 访问表
    visited=[[False]*m for _ in range(n)]
    
    res=0 # 用来记录岛屿的数量
    for i in range(n): # 遍历行
        for j in range(m): # 遍历列
            # 判断：如果当前节点是陆地，res+1并标记访问该节点，使用深度搜索标记相邻陆地
            if grid[i][j]==1 and not visited[i][j]:
                res+=1 # 记录岛屿数量
                visited[i][j]=True # 记录已经访问过该节点
                dfs(grid,visited,i,j)
    print(res)

if __name__=='__main__':
    main()