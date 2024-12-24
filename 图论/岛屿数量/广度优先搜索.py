# BFS和DFS的区别
# 1. BFS使用队列deque，节点以先入先出的方式处理，保证先处理当前层次的节点，再处理下一层次的节点
#    DFS使用栈，节点以后入先出方式处理，保证深入一个路径直至叶子节点后再回溯
# PS：
# 为什么BFS用队列：因为BFS的核心是按照层次遍历节点，也就是先处理与节点距离比较近的节点，然后逐步扩展到更远的节点
# 为什么DFS用栈：DFS的核心是沿着一条路径不断深入到最远节点，符合栈的后入先出的规则

# 2. 遍历顺序：BFS是层次遍历，逐层扩展；DFS是深度遍历，沿着一条路径深入到最远的节点，然后回溯

from collections import deque
directions=[[0,1],[1,0],[0,-1],[-1,0]] # 方向数组

def bfs(grid,visited,x,y):
    """
        在二维网格grid中，从起点[x,y]开始，遍历与之相邻的所有符合条件的块
        BFS要先处理当前层的所有节点，然后再处理下一层的节点。队列的先进先出性质确保了最先加入的节点会先被处理。
    """
    que=deque([]) # 双端队列，表示BFS开始从该点扩展
    que.append([x,y]) 
    while que:
        # 处理当前待访问的节点，并从队列中移除它
        cur_x,cur_y=que.popleft() # 取出队首元素cur_x, cur_y，作为当前正在处理的点
        # 尝试向四个方向扩展
        for i,j in directions:
            next_x=cur_x+i
            next_y=cur_y+j
            # 越界，不访问（检查边界条件）
            if next_y<0 or next_x<0 or next_x>=len(grid) or next_y>=len(grid[0]):
                continue
            # 检查访问条件（如果邻居未被访问并且为陆地块，将其标记为已访问，并加入队列）
            if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                visited[next_x][next_y]=True
                que.append([next_x,next_y])

def main():
    n,m=map(int,input().split())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))
    visited=[[False]*m for _ in range(n)]
    res=0
    for i in range(n): # 遍历行
        for j in range(m): # 遍历列
            # 判断是否是岛屿，以及是否遍历过
            if grid[i][j]==1 and not visited[i][j]:
                res+=1
                bfs(grid,visited,i,j)
    print(res)
    
if __name__=='__main__':
    main()