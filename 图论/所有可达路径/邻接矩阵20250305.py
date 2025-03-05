# 时间复杂度：O(n^n)
# 1. 图的初始化：O(n^2) 有n+1行 每行有n+1个元素
# 2. 边信息的读取和存储：每个循环会执行m次，O(m)
# 3. 深度优先搜索：对于一个有n个节点的图，每个节点最多会被访问一次，并且每个访问时会尝试n个可能得邻接节点 O(n^n)

# 空间复杂度：O(nxn!)
# 1. 图的存储：O(n^2)
# 2. 递归调用栈：深度优先搜索过程中递归调用栈的深度最大为O(n)
# 3. 路径存储：节点1到节点n的路径，最坏情况下有n!条不同的路径，每条路径最多包含n个节点，此时为O(nxn!)（比如完全图的情况）


def main():
    n, m=map(int, input().split())
    # n个节点，m条边
    graph=[[0]*(n+1) for _ in range(n+1)]

    for _ in range(m):
        s, t=map(int, input().split())
        graph[s][t]=1
        # 表示s到t之间有一条边
    
    result=[]
    dfs(graph, 1, n, [1], result)

    # 如果没找到节点1到节点n的路径，则返回-1
    if not result:
        print(-1)
    # 如果找到了路径，则输出路径值
    else:
        for path in result:
            print(' '.join(map(str, path)))

def dfs(graph, x, n, path, result):
    # 类似于用回溯算法来找路径
    if x==n:
        result.append(path[:])
        return
    for i in range(1, n+1):
        if graph[x][i]==1:
            path.append(i)
            dfs(graph, i, n, path, result)
            path.pop()

if __name__=='__main__':
    main()



