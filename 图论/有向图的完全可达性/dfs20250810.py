n, k = map(int, input().split())
grid = [[] for _ in range(n+1)]
for i in range(k):
    s, t = map(int, input().split())
    grid[s].append(t)

visited = [False]*(n+1) # 表示是否能遍历到第i个节点
visited[0]= True

def dfs(node, visited, grid):
    visited[node] = True
    for neighbor in grid[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(neighbor, visited, grid)

dfs(1, visited, grid)
for i in range(1, n+1):
    if not visited[i]:
        print(-1)
        exit()
print(1)