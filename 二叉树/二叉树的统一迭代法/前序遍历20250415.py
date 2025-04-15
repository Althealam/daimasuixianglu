# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        st=[]
        if root:
            st.append(root)
        while st:
            node=st.pop()
            if node!=None:
                if node.right:
                    st.append(node.right) # 右
                if node.left:
                    st.append(node.left) # 左
                st.append(node) # 中
                st.append(None)
            else:
                node=st.pop()
                result.append(node.val)
        return result
