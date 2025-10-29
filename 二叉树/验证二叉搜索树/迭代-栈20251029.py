# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = []
        cur = root
        pre = None
        # 中序遍历 用空节点来标记中间节点
        while stack or cur is not None:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else: # 遇到空节点
                cur = stack.pop()
                if pre is not None and pre.val>=cur.val: # 当前遍历的节点值要超过之前的节点 也就是中见节点的值超过左节点的值
                    return False
                pre = cur
                cur = cur.right 
        return True