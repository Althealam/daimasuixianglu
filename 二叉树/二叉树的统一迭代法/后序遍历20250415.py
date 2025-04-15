# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        st=[]
        if root:
            st.append(root)
        while st:
            node=st.pop()
            if node!=None:
                st.append(node) # 中
                st.append(None) # 空
                if node.right: # 右
                    st.append(node.right)
                if node.left: # 左
                    st.append(node.left)
            else:
                node=st.pop()
                result.append(node.val)
        return result