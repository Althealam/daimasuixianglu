# 方法：迭代法
# 分析：
# 1. 如果要删除的节点小于low，那么其左子树也需要删除，但是其右子树可能是需要保留的
# 2. 如果要删除的节点大于high，那么其右子树也需要删除，但是其左子树可能是需要保留的

# 时间复杂度：O(n)
# 在修剪过程中，每个节点会被访问一次，并且做出是否保留、修剪左子树、或修剪右子树的判断

# 空间复杂度：O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self,root,low,high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: Optional[TreeNode]
        """
        if not root:
            return root
        # 处理头节点，让root移动到[L,R]范围内，注意是左闭右闭
        while root and (root.val<low or root.val>high):
            if root.val<L:
                root=root.right # 小于L往右走
            else:
                root=root.left # 大于R往左走
        cur=root

        # 此时root已经在[L,R]范围内，处理左孩子元素小于L的情况
        while cur:
            while cur.left and cur.left.val<low:
                cur.left=cur.left.right
            cur=cur.left
        
        cur=root

        # 此时root已经在[L,R]范围内，处理右孩子大于R的情况
        while cur:
            while cur.right and cur.right.val>high:
                cur.right=cur.right.left
            cur=cur.right
        
        return root