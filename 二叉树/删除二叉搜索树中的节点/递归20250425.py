# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1. 要删除的节点为叶子节点：返回None
# 2. 要删除的节点有左孩子，没有右孩子：返回root.left
# 3. 要删除的节点没有左孩子，有右孩子：返回root.right
# 4. 要删除的节点有左孩子也有右孩子：将删除节点的左子树头节点放在删除节点的右子树的最左边节点的左孩子上
# （1）找到要删除的节点的右子树的最左边节点的左孩子

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        # 查找key所在的位置
        if root.val>key: # key在root的左子树
            root.left=self.deleteNode(root.left, key)
        elif root.val<key: # key在root的右子树
            root.right=self.deleteNode(root.right, key)
        elif root.val==key:
            if root.left is None and root.right is None:
                return None
            elif root.left is not None and root.right is None:
                return root.left
            elif root.left is None and root.right is not None:
                return root.right
            elif root.left is not None and root.right is not None:
                # 查找要删除的节点的右子树的最左边节点的左孩子
                cur=root.right
                while cur.left:
                    cur=cur.left
                cur.left=root.left
                return root.right
        return root
        