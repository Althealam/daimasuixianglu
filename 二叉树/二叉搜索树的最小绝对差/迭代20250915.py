# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = self.inorder(root)
        ans = float('inf')
        for i in range(1, len(res)):
            ans = min(ans, res[i]-res[i-1])
        return ans
    
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