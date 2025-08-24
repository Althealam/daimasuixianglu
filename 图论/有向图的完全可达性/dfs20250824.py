n, k = map(int, input().split()) # 节点数量N的边的数量
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    s, t = map(int, input().split())
    graph[s][t] = 1

def find_path(n, graph):
    visited = [False]*n
    visited[0] = True
    def dfs(node, visited):
        visited[node] = True
        for i in range(n):
            if not visited[i] and graph[node][i]==1:
                visited[i]=True
                dfs(i, visited)
    dfs(1, visited)
    for i in range(n):
        if visited[i]==False:
            print(-1)
            exit()
    print(1)

find_path(n, graph)
        