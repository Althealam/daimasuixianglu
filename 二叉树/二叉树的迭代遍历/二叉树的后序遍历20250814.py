# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 左右中==>中左右
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        st = []
        st.append(root)
        while st:
            node = st.pop()
            res.append(node.val)
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        return res[::-1]

        