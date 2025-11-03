# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        st = []
        cur = root
        pre = 0
        while cur or st:
            if cur: # find the right node of the tree
                st.append(cur)
                cur = cur.right
            else: # already achieve the right node of the tree
                cur = st.pop()
                cur.val+=pre
                pre = cur.val
                cur = cur.left
        return root

            

        