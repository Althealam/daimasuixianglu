# 题意：在0, 1, 2, ..., 2n-1中选出n个数，填入左括号，其余n位置填入右括号
# 改进方法：在序列仍然保持有效的时候才添加(或者)，而不是像暴力法一样每次都添加括号
# 时间复杂度：O(4**n/n**(1/2))
# 空间复杂度：O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = [] # 存储答案值
        left, right = 0, 0 # 分别表示左右括号的数量
        self.traversal(ans, n, left, right, [])
        return ans
    
    def traversal(self, ans, n, left, right, path):
        if len(path)==2*n:
            ans.append(''.join(path[:]))
            return 
        if left<n:
            path.append('(')
            self.traversal(ans, n, left+1, right, path)
            path.pop()
        if right<left:
            path.append(')')
            self.traversal(ans, n, left, right+1, path)
            path.pop()