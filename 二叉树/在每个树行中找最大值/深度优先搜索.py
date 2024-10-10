# 方法：深度优先搜索
# 思路：用树的先序遍历来进行深度优先搜索，并用curHeight来标记遍历到的当前节点的高度。
# 当遍历到curHeight高度的节点就判断是否更新该层节点的最大值。
# 时间复杂度：O(n)，其中n为二叉树节点个数（二叉树的遍历中每个节点会被访问并且只会被访问一次）
# 空间复杂度：O(height)，其中height表示二叉树的高度。递归函数需要栈空间，而栈空间取决于递归的深度，最坏情况下为O(n)（height<=n）

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans=[]
        def dfs(node,curHeight):
            if node is None:
                return
            if curHeight==len(ans):
                ans.append(node.val)
            else:
                ans[curHeight]=max(ans[curHeight],node.val)
            dfs(node.left,curHeight+1)
            dfs(node.right,curHeight+1)
        dfs(root,0)
        return ans
        