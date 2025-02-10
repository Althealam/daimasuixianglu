# 思路：
# 1. 如果root1为空，则返回root2
# 2. 如果root2为空，则返回root1
# 3. 如果root1和root2都不为空，则返回root1+root2
# 4. 如果root1和root2都为空，则返回空

# 时间复杂度：O(n) n是两棵树中节点数的最大值，因为需要遍历两棵树的节点
# 空间复杂度：O(h) 其中h是两棵树中高度的最大值 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # 中
        if root2 and not root1:
            return root2
        if root1 and not root2:
            return root1
        if not root1 and not root2:
            return None
        root=TreeNode()
        root.val=root1.val+root2.val # 如果root1和root2都不为空，则合并当前节点的值
        # 注意，不可以通过以下代码实现：
        # if root1 and root2:
        #    returnv TreeNode(root1.val+root2.val)
        # 这种情况只是简单的返回了一个新节点，实际上这个节点没有放到任何一个节点后面
        root.left=self.mergeTrees(root1.left, root2.left) # 左
        root.right=self.mergeTrees(root1.right, root2.right) # 右
        return root
        
        