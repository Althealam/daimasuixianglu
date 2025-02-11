# 思路：
# 1. 没有找到需要修剪的节点，返回None
# 2. root.val<low：root的左子树也一定小于low，可以直接剪去，检查右子树即可
# 3. root.val>low：root的右子树也一定大于low，可以直接剪去，检查左子树即可

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：修剪过程中需要遍历二叉搜索树中的每个节点，判断该节点的值是否在区间内，因此是O(n)
# 空间复杂度：取决于递归调用栈的深度，O(h)

class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: Optional[TreeNode]
        """
        if root is None:
            return None
        
        # 寻找符合区间[low, high]的节点
        if root.val<low:
            return self.trimBST(root.right, low, high)
        elif root.val>high:
            return self.trimBST(root.left, low, high)
        
        # 递归修剪左右子树
        root.left=self.trimBST(root.left, low, high)
        root.right=self.trimBST(root.right, low, high)
        return root
        