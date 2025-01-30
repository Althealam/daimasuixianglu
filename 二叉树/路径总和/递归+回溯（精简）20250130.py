# 思路：个人理解就是找二叉树的所有路径，以及判断每条路径是否值的和为目标和，如果是的话则直接返回True

# 时间复杂度：O(n)
# 空间复杂度：递归调用栈的空间+存储路径的列表空间
# 1. 递归调用栈的空间：最坏情况下二叉树退化为链表，此时为O(n)；最好情况下为平衡二叉树，则为O(log2n)
# 2. 存储路径的列表空间：path最多存储从根节点到叶子节点的所有节点，其长度同样取决于二叉树的高度h，道理同上

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.left is None and root.right is None and root.val==targetSum:
            return True
        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

solution=Solution()
result=solution.hasPathSum(root,4)
print(result)