## 本题在字节筋斗云面试中考察过，但是没能成功写出来
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False]*n for _ in range(m)]
        directions = [[0, 0], [0, 1], [1, 0], [0, -1], [-1, 0]] # 增加一个[0,0]值用于遍历自己
        all_word = []
        def dfs(x, y, board, visited, word, path):
            for dx, dy in directions:
                next_x, next_y = dx+x, dy+y
                if next_x<0 or next_y<0 or next_x>m-1 or next_y>n-1:
                    continue
                if visited[next_x][next_y]==True:
                    continue
                if next_x>=0 and next_y>=0 and next_x<=m-1 and next_y<=n-1:
                    visited[next_x][next_y] = True
                    path.append(board[next_x][next_y])
                    all_word.append(''.join(path[:]))
                    dfs(next_x, next_y, board, visited, word, path)
                    path.pop()
                    visited[next_x][next_y] = False
        
        for i in range(m):
            for j in range(n):
                dfs(i, j, board, visited, word, [])
        if word in all_word:
            return True
        return False




