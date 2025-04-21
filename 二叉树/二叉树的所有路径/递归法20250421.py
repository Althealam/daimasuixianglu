# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 分析：由于本题是需要路径，因此需要前序遍历（从根节点到叶子节点）
# 时间复杂度：O(n)
# 1. 遍历过程：DFS遍历二叉树的每个节点，对于每个节点都会执行一次路径的添加和回溯操作：O(n)
# 2. 节点数量：假设二叉树的节点总数为n，由于代码需要访问二叉树中的每个节点恰好一次，因此遍历操作的时间复杂度为O(n)
# 3. 路径拼接：对于每个叶子节点，代码会将当前路径拼接成字符串并添加到结果列表中：O(n)

# 空间复杂度：O(n**2)
# 1. 递归调用栈：DFS递归调用栈的深度取决于二叉树的高度，最坏情况下二叉树退化为链表，递归调用栈的深度为O(n)
# 2. 结果列表：结果列表存储从根节点到叶子节点的所有路径，最坏情况下二叉树的每个节点都是叶子节点，此时结果列表会存储O(n)条路径，每条路径的长度最多为O(n)，因此结果列表占用的空间是O(n**2)

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
    

        