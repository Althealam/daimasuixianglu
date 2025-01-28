
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.getheight(root)!=-1


    def getheight(self,node):
        # bad case
        if not node:
            return 0
        # 左子树
        left=self.getheight(node.left)
        # 右子树
        right=self.getheight(node.right)
        # 不是平衡二叉树的情况
        if left==-1 or right==-1 or abs(left-right)>1:
            return -1
        # 计算二叉树的高度
        return max(left, right)+1 
