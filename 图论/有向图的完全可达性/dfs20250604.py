# 思路：有向图搜索全路径
# DFS三部曲：
# 1. 确定递归函数，参数
# 2. 确定终止条件
# 3. 处理目前搜索节点出发的路径

def dfs(graph, i, visited):
    """
    dfs搜索当前节点i的邻居节点
    搜到了邻居节点则将该节点的visited设置为True
    """
    for neighbor in graph[i]:
        if not visited[neighbor]:
            visited[neighbor]=True
            dfs(graph, neighbor, visited)


def main():
    # n为节点数量，k为边的数量
    n, k = map(int, input().split())
    # 构建有向图矩阵，表示每个节点的连接节点
    graph=[[] for _ in range(n+1)]
    for _ in range(k):
        s, t = map(int, input().split())
        graph[s].append(t)

    # 构建访问表
    visited=[False]*(n+1)
    visited[1]=True


    # 从节点1开始搜索
    dfs(graph, 1, visited)

    for i in range(1, n+1): # 遍历节点
        if not visited[i]: # 有些节点没有访问过，则表示1无法到达该节点
            print(-1)
            return 
    print(1)

if __name__=='__main__':
    main()
