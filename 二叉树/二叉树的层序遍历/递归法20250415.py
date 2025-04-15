# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels=[] # 存储层序遍历的值
 
        def traversal(node, level):
            if not node:
                return 
            if len(levels)==level:
                levels.append([])
            
            # 中
            levels[level].append(node.val)
            # 左
            traversal(node.left, level+1)
            # 右
            traversal(node.right, level+1)
        
        traversal(root, 0) # 从第一层开始遍历
        return levels