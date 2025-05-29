def main():
    # n个节点，m条边
    n, m=map(int, input().split())

    #### 构建邻接表
    graph=[[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        s, t=map(int, input().split())
        graph[s][t]=1

    #### 获取所有的路径
    result=[]
    dfs(graph, 1, n, [1], result)

    for path in result:
        print(' '.join(map(str, path)))

def dfs(graph, x, n, path, result):
    """
    :param graph：邻接表
    :param x: 当前遍历的节点
    :param n: 终点
    :param path: 当前遍历的路径
    :param result: 结果集
    """
    # 终止条件：到达了终点
    if x==n:
        result.append(path[:])
        return 
    for i in range(1, n+1):
        # 当前遍历的节点x到i有边
        if graph[x][i]==1:
            path.append(i)
            # 回溯
            dfs(graph, i, n, path, result)
            path.pop()

if __name__=='__main__':
    main()