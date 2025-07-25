# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 没找到要删除的节点，遍历到空节点直接返回
# 2. 找到要删除的节点，并且其左右孩子都为空，则直接删除
# 3. 找到要删除的节点，并且其左孩子为空，右孩子不为空，删除节点，右孩子补位，返回右孩子为根节点
# 4. 找到要删除的节点，并且其左孩子不为空，右孩子为空，删除其节点，左孩子补位，返回左孩子为根节点
# 5. 找到要删除的节点，该节点的左右孩子都不为空，删除节点的左孩子，放到节点的右子树的最左边的左孩子节点上，返回删除节点的右孩子为根节点
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val==key:
            if root.left is None and root.right is None:
                return None
            elif root.left is None and root.right is not None:
                return root.right
            elif root.left is not None and root.right is None:
                return root.left
            elif root.left is not None and root.right is not None:
                # 找到右孩子节点的最左节点
                node = root.right
                while node.left:
                    node = node.left
                node.left = root.left
                return root.right
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root
        