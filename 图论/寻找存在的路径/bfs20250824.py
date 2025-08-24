from collections import deque
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
    def bfs(node, destination, visited):
        queue = deque()
        visited[node] = True
        queue.append(node)
        while queue:
            cur_node = queue.popleft()
            if cur_node == destination:
                print(1)
                exit()
            for i in range(n):
                if not visited[i] and grid[cur_node][i]==1:
                    visited[i] = True
                    bfs(i, destination, visited)

    
    bfs(source, destination, visited)
    print(0)
    exit()

find_path(n, source, destination, grid)


