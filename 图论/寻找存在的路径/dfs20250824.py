n, m = map(int, input().split())
grid = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    s, t = map(int, input().split())
    grid[s][t] = 1
    grid[t][s] = 1
source, destination = map(int, input().split())

def find_path(n, source, destination, grid):
    if source==destination:
        print(1)
        exit()
    
    visited = [False]*n
    def dfs(node, destination, visited):
        if node == destination:
            print(1)
            exit()
        for i in range(n):
            if not visited[i] and grid[node][i] == 1:
                visited[i] = True
                dfs(i, destination, visited)
    
    dfs(source, destination, visited)
    print(0)
    exit()

find_path(n, source, destination, grid)


