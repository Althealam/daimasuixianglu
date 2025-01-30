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
    def traversal(self, cur, path, targetSum):
        path.append(cur.val)

        # 到达了叶子节点，开始判断path的和是否是targetSum
        if cur.left is None and cur.right is None:
            if sum(path)==targetSum:
                return True
            else:
                return False
        # 需要记录下来左右的返回值
        left_result=False
        right_result=False
        if cur.left:
            left_result=self.traversal(cur.left, path, targetSum)
            path.pop()
        if cur.right:
            right_result=self.traversal(cur.right, path, targetSum)
            path.pop()
        return left_result or right_result

    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        path=[] # 记录当前路径的节点和
        if root is None:
            return False
        return self.traversal(root,path,targetSum)         


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

solution=Solution()
result=solution.hasPathSum(root,4)
print(result)