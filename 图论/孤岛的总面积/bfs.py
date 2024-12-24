# 方法：BFS
# 思路：
# 从周边找陆地，通过dfs或者bfs将周边靠陆地并且相邻的陆地都变成海洋，然后再重新遍历图
# 统计此时还剩下的陆地即可

from collections import deque

# 处理输入
n,m=list(map(int,input().split())) # 网格的行数和列数
g=[] # 二维列表，表示输入的网格
for _ in range(n):
    row=list(map(int,input().split()))
    g.append(row)

# 定义四个方向
directions=[[0,1],[1,0],[-1,0],[0,-1]]
count=0

# 广搜
def bfs(r,c): # 起点的行列坐标为(r,c)
    global count
    q=deque() # 用于存储待访问的节点
    q.append((r,c)) # 将起点加入队列
    g[r][c]=0 # 将当前位置标记为海洋
    count+=1 # 记录访问的节点数
    
    while q:
        r,c=q.popleft() # 从队列中取出当前节点
        for di in directions: # 遍历四个方向
            next_r=r+di[0]
            next_c=c+di[1]
            # 判断是否越界或者不是陆地
            if next_c<0 or next_c>=m or next_r<0 or next_r>=n:
                continue
            if g[next_r][next_c]==1: # 如果是陆地，继续搜索
                q.append((next_r,next_c)) # 将新的陆地加入队列
                g[next_r][next_c]=0 # 标记为海洋
                count+=1 # 更新计数器

def main():
    # 第一步：清理边界相连的陆地（不会清理到孤岛）
    for i in range(n): # 遍历左、右边界
        if g[i][0]==1: # 左边界
            bfs(i,0)
        if g[i][m-1]==1: # 右边界
            bfs(i,m-1)
    for i in range(m): # 遍历上、下边界
        if g[0][i]==1: # 上边界
            bfs(0,i)
        if g[n-1][i]==1: # 下边界
            bfs(n-1,i)
    
    # 第二步：统计剩余的独立陆地
    count=0 # 初始化剩余陆地计数器
    for i in range(n):
        for j in range(m):
            if g[i][j]==1: # 找到一个新的陆地
                bfs(i,j)
    print(count)

if __name__=='__main__':
    main()