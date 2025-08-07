class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0]) if rows>0 else 0

        visited = [[False for _ in range(cols)] for _ in range(rows)]

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        all_subwords = set() # 存储所有可能的子单词

        def dfs(row, col, current_word):
            """
            深度优先搜索
            row, col: 当前位置
            index: 当前匹配到的单词索引
            """
            all_subwords.add(current_word)

            if len(current_word)>=len(word):
                return 
            
            for dx, dy in directions:
                new_row, new_col = row+dx, col+dy
                if 0<=new_row<rows and 0<=new_col<cols and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    dfs(new_row, new_col, current_word+board[new_row][new_col])
                    visited[new_row][new_col] = False

        for i in range(rows):
            for j in range(cols):
                visited[i][j]=True
                dfs(i, j, board[i][j])
                visited[i][j]=False # 回溯
        
        return word in all_subwords
        
board = [['A', 'B', 'C'], ['D', 'E', 'F']]
test_word = 'ABC'
sol = Solution()
res = sol.exist(board, test_word)
print(res)