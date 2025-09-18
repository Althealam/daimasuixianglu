n, m = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    s, t = map(int, input().split())
    graph[s][t] = 1

result = []

def dfs(graph, x, n, path, result):
    if x==n:
        result.append(path[:])
    for i in range(1, n+1):
        if graph[x][i]==1:
            path.append(i)
            dfs(graph, i, n, path, result)
            path.pop()

dfs(graph, 1, n, [1], result)
if not result:
    print(-1)
else:
    for path in result:
        print(' '.join(map(str, path)))