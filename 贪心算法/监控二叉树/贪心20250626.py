# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 选或者不选
# 1. 选：在这个节点安装摄像头
# 2. 不选：在其父节点/左右儿子节点安装摄像头

# 每个节点有三种状态
# 1. 蓝色：安装摄像头
# 2. 黄色：不安装摄像头，并且它的父节点安装摄像头
# 3. 红色：不安装摄像头，并且它的至少一个儿子节点装摄像头

# 我们需要讨论三种情况：子树根节点为蓝色时，这颗子树最少需要多少摄像头；子树根节点为黄色时，这颗子树最少需要多少摄像头；子树根节点为红色时，这颗子树最少需要多少摄像头
# 蓝色=min(左蓝, 左黄, 左红)+min(右黄, 右蓝, 右红)+1
# 黄色=min(左蓝, 左红)+min(右蓝, 右红)（黄色节点的儿子不可能是黄色，否则代表儿子节点的父节点安装了摄像头）
# 红色=min(左蓝+右红, 左红+右蓝, 左蓝+右蓝)（红色节点的儿子不可能是黄色，并且至少有一个儿子是蓝色）
# 最终答案=min(根节点为蓝色，根节点为红色)
# 递归边界：1. 空节点不能装摄像头，蓝色为正无穷，表示不合法；2. 空节点不需要被监控，黄色和红色都为0

# 时间复杂度：O(n)
# 空间复杂度：O(n)

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return inf, 0, 0 # 红黄蓝
            l_choose, l_by_father, l_by_son = dfs(node.left)
            r_choose, r_by_father, r_by_son = dfs(node.right)
            choose = min(l_choose, l_by_father, l_by_son)+min(r_choose, r_by_father, r_by_son)+1
            by_father = min(l_choose, l_by_son)+min(r_choose, r_by_son)
            by_son = min(l_choose+r_by_son, l_by_son+r_choose, l_choose+r_choose)
            return choose, by_father, by_son
        choose, _ , by_son = dfs(root)
        return min(choose, by_son)
