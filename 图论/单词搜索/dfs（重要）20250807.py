# 思路：以(i, j)为起点开始搜索，定义dfs(i, j, k)表示在当前board[i][j]这个格子，要匹配word[k]，返回在这个状态下最终能否匹配成功
# （1）board[i][j]!=word[k]: 匹配失败，返回False
# （2）k=len(word)-1，匹配成功，返回True
# （3）枚举(i, j)周围的四个相邻格子(x, y)，如果(x, y)没有出界，则递归dfs(x, y, k+1)，如果其返回True，则dfs(x, y, k)也返回True
# （4）如果递归周围的四个相邻格子都没有返回True，则最后返回False，表示没有搜索到
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(i, j, k):
            if board[i][j]!=word[k]: # 匹配失败
                return False
            if k==len(word)-1: # 匹配成功
                return True
            board[i][j] = '' # 表示访问过
            for dx, dy in directions:
                next_x = dx+i
                next_y = dy+j
                if 0<=next_x<m and 0<=next_y<n and dfs(next_x, next_y, k+1):
                    return True
            board[i][j] = word[k] # 恢复现场
            return False # 没有搜索到
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
            