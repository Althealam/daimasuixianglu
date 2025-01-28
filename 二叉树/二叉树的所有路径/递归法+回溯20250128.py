# 递归法

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def traversal(self, cur, path, result):
        path.append(cur.val) # 中
        
        # 到达了叶子节点，就把这条路径做连接处理，然后将这条路径添加到结果集中
        if not cur.left and not cur.right:
            sPath='->'.join(map(str,path)) # 把path处理成字符串
            result.append(sPath)
            return

        if cur.left: # 左
            self.traversal(cur.left, path, result)
            path.pop() # 回溯

        if cur.right: # 右
            self.traversal(cur.right, path, result)
            path.pop() # 回溯


    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        result=[] # 记录所有路径
        path=[] # 当前节点
        if not root:
            return result
        self.traversal(root, path, result)
        return result

# 构建一个简单的测试二叉树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

solution = Solution()
solution.binaryTreePaths(root)
print("Final result:", solution.binaryTreePaths(root))