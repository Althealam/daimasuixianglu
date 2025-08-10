n, m = map(int, input().split())
grid = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s, t = map(int, input().split())
    grid[s][t]=1


ans = []
def dfs(grid, node, n, path, ans):
    if node==n:
        ans.append(path[:])
        return 
    for i in range(1, n+1):
        if grid[node][i]==1:
            path.append(i)
            dfs(grid, i, n, path, ans)
            path.pop()
dfs(grid, 1, n, [1], ans)
for path in ans:
    print(' '.join(map(str, path)))

