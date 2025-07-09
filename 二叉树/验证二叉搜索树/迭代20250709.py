# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = self.inorder(root)
        for i in range(1, len(res)):
            if res[i]-res[i-1]<=0:
                return False
        return True
    
    def inorder(self, root):
        if not root:
            return []
        st = [root]
        res = []
        while st:
            node = st.pop()
            if node:
                if node.right:
                    st.append(node.right)
                st.append(node)
                st.append(None)
                if node.left:
                    st.append(node.left)
            else:
                node = st.pop()
                res.append(node.val)
        return res
            
            