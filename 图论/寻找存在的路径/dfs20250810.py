n, m = map(int, input().split())
grid = [[] for _ in range(n+1)]
for _ in range(m):
    s, t = map(int, input().split())
    grid[s].append(t)
    grid[t].append(s)

source, destination = map(int, input().split())

visited = [False]*(n+1)
found = False
def dfs(node, grid, destination):
    global found
    if node==destination:
        found = True
        print(1)
        exit()
    for neighbor in grid[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(neighbor, grid, destination)

dfs(source, grid, destination)
if not found:
    print(0)
    exit()