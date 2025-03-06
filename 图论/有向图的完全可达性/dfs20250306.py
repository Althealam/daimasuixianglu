# 时间复杂度：O(n^2+k)
# 1. 输入处理：O(n^2) grid矩阵是nxn的
# 2. 处理边信息：O(k)
# 3. dfs部分：O(n+k)
# （1）对图中的每个节点和每条边进行访问，最坏情况下图是一个完全有向图，每个节点都和其他所有节点相连，此时的边的数量为n(n-1)，但是一般情况下边的数量为k
# （2）每个节点最多被访问一次，总共n个节点，对于每条边最多会被访问一次，总共k条变

# 空间复杂度：O(n^2)
# 1. 邻接矩阵：O(n^2)
# 2. 访问标记数组：O(n)
# 3. 递归调用栈：DFS递归调用栈的深度是n


def main():
    # 处理输入数据
    n, k=map(int, input().split())

    grid=[[0]*n for _ in range(n)]

    for _ in range(k):
        s, t=map(int, input().split())
        grid[s-1][t-1]=1

    visited=[False]*n # 记录是否遍历到该节点

    visited[0]=True # 第一个节点一定是遍历过的
    dfs(grid, 0, visited) # 开始遍历有向图，获取visited矩阵

    # 如果有没遍历过的节点，那么就直接返回-1
    for i in range(n):
        if not visited[i]:
            print(-1)
            return
    # 如果所有节点都遍历过了，则直接返回1
    print(1)


def dfs(grid, key, visited):
    for i in range(len(grid[key])):
        # 如果从key到i有边并且i节点未被访问过
        if grid[key][i]==1 and not visited[i]:
            visited[i]=True
            # 判断节点i是否可以到其他的节点，如果可以的话，那么这个其他的节点也会是True
            dfs(grid, i, visited)
    

if __name__=='__main__':
    main()