# 时间复杂度：O(m+n)
# 1. 输入处理：O(m)
# 2. BFS：O(m+n)

# 空间复杂度：O(n^2)
# 1. 邻接矩阵：O(n^2)
# 2. 访问标记数组：O(n)
# 3. 队列：O(n)

from collections import deque
def main():
    # 处理输入
    n, m=map(int, input().split())
    # n是节点数
    # m是边数

    # 处理邻接矩阵
    grid=[[0]*n for _ in range(n)]
    for i in range(m):
        s, t=map(int, input().split())
        # 由于是无向图，因此两个都需要设置为1
        grid[s-1][t-1]=1
        grid[t-1][s-1]=1

    # 处理source和destination的输入
    source, destination=map(int, input().split())
    
    # 需要适应grid的大小，因此需要减去1
    source-=1
    destination-=1
    
    # 访问矩阵
    visited=[False]*n
    # 利用队列判断source是否可以到destination
    queue=deque([source])
    visited[source]=True
    while queue:
        node=queue.popleft()
        if node==destination:
            print(1)
            return 
        for neighbor in range(n):
            if grid[node][neighbor]==1 and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor]=True
    print(0)


            
if __name__=='__main__':
    main()
    
