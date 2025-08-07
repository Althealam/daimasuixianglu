land = [
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]


def shuiyudaxiao(land):
    ans = [] # 记录所有水域的大小
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    m, n = len(land), len(land[0])
    visited = [[False]*n for _ in range(m)]

    def dfs(i, j):
        current_area = 1
        visited[i][j]=True
        # 注意：如果前面定义了current_area和对i和j的操作，那么后面就不需要定义
        for dx, dy in directions:
            next_x, next_y = i+dx, j+dy
            if next_x<0 or next_y<0 or next_x>=m or next_y>=n:
                continue
            if not visited[next_x][next_y] and land[next_x][next_y]==0:
                current_area+=dfs(next_x, next_y)
        return current_area
    
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and land[i][j]==0:
                current_area=dfs(i, j)
                ans.append(current_area)
    return ans

ans = shuiyudaxiao(land)
print(ans)
