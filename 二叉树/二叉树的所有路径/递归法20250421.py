# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 分析：由于本题是需要路径，因此需要前序遍历（从根节点到叶子节点）


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result=[]
        self.traversal(root, [], result)
        return result

    def traversal(self, cur, path, result):
        """
        :param cur: 当前正在遍历的节点
        :param path: 当前正在遍历的路径
        :param result: 存储所有路径的结果集
        """
        path.append(cur.val)
        if cur.left is None and cur.right is None: # 遇到了叶子节点
            result.append('->'.join(map(str, path)))
            return
        if cur.left:
            self.traversal(cur.left, path, result)
            path.pop()
        if cur.right:
            self.traversal(cur.right, path, result)
            path.pop()
    

        