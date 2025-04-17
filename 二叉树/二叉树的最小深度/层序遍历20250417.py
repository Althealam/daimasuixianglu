# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：自顶向下求解，通过dfs来求解最小深度

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=collections.deque([root])
        min_depth=0
        while queue:
            min_depth+=1 # 每次进入一层时就更新min_depth的值
            for _ in range(len(queue)):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if node.left is None and node.right is None: # 到达叶子节点时则直接返回深度
                    return min_depth
        return min_depth
