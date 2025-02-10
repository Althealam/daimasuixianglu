# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            # 检查左子树，并且更新上界为当前节点的值
            if not helper(node.left, lower, val):
                return False
            # 检查右子树，并且更新下界为当前节点的值
            if not helper(node.right, val, upper):
                return False
            return True
        return helper(root)

# 构建二叉树 root = [2, 1, 3]
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

solution = Solution()
result = solution.isValidBST(root)
print(result)