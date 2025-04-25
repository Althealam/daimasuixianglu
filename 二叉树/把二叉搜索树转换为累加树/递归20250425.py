# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 遍历顺序是右中左
# 定义一个pre来记录上一个节点的值，用递归来处理节点，先处理cur.right，再处理中节点，再最后出现左节点

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre=0 # 前一个节点的数值
        self.traversal(root)
        return root
    
    def traversal(self, cur):
        if cur is None:
            return 
        self.traversal(cur.right)
        cur.val+=self.pre
        self.pre=cur.val
        self.traversal(cur.left)

        