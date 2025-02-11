# 思路：
# 1. 没找到要删除的节点，遍历到空节点直接返回
# 2. 找到要删除的节点，并且该节点的左右孩子都为空，则直接删除，返回Null为根节点
# 3. 找到要删除的节点，该节点的左孩子为空，右孩子不为空，删除节点，右孩子补位，返回右孩子为根节点
# 4. 找到要删除的节点，该节点的右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
# 5. 找到要删除的节点，该节点的左右孩子都不为空，删除节点的左孩子，放到节点的右子树的最左边的左孩子节点上，返回删除节点的右孩子为根节点

# 时间复杂度：O(h)
# 1. 查找要删除的节点：最多遍历树的高度h个节点（根据key与当前节点的大小关系来递归查找）
# 2. 处理删除节点后的树结构调整：处理左右子节点不为空时，需要找到右子树的最左边节点，此时最多需要遍历树的高度h个节点

# 空间复杂度：O(h)
# 取决于递归调用栈的深度，而递归调用栈的深度和树的高度相关

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        # 没找到要删除的节点
        if root is None:
            return None
        
        # 找到了要删除的节点
        if root.val==key:
            # 1. 要删除的节点的左右孩子都为空
            if root.left is None and root.right is None:
                return None
            # 2. 要删除的节点的左孩子为空，右孩子不为空
            elif root.left is None and root.right is not None:
                return root.right
            # 3. 要删除的节点的左孩子不为空，右孩子为空
            elif root.left is not None and root.right is None:
                return root.left
            # 4. 要删除的节点的左右孩子都不为空
            else:
                # 找到要删除的节点的右子树的最左边的节点
                cur=root.right
                while cur.left is not None:
                    cur=cur.left
                # 将要删除的右子树的最左边的节点连接要删除的节点的左子树
                cur.left=root.left
                return root.right

        # 判断要删除的节点在左右子树的哪棵树上 
        if root.val>key:
            root.left=self.deleteNode(root.left, key)
        elif root.val<key:
            root.right=self.deleteNode(root.right, key)
        return root


        