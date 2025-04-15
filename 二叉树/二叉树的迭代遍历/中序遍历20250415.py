# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack=[]
        result=[]
        cur=root
        while cur or stack:
            # 迭代访问最底层的左节点
            if cur:
                stack.append(cur)
                cur=cur.left
            # 到达最左节点后处理栈顶节点
            else:
                cur=stack.pop()
                result.append(cur.val)
                # 取栈顶元素右节点
                cur=cur.right
        return result