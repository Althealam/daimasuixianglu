# 时间复杂度：O(n+m)
# 1. 输入处理：O(m)
# 2. dfs部分：O(n+m)

# 空间复杂度：O(n**2)
# 1. 邻接矩阵：O(n**2)
# 2. 访问标记数组：O(n)
# 3. 递归调用栈：O(n)
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
    # 判断source是否可以到destination
    if dfs(source, visited, destination, grid, n):
        print(1)
    else:
        print(0)



def dfs(node, visited, destination, grid, n):
    if node==destination:
        return True
    visited[node]=True
    for neighbor in range(n):
        if grid[node][neighbor]==1 and not visited[neighbor]:
            if dfs(neighbor, visited, destination, grid, n):
                return True
    return False



            
if __name__=='__main__':
    main()
    
