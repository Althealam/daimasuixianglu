class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

# 左中右--栈：右中左
class Solution:
    def inorderTraversal(self, root):
        result=[]
        st=[]
        if root:
            st.append(root)
        while st:
            node=st.pop()
            if node!=None:
                if node.right:
                    st.append(node.right)
                
                st.append(node)
                st.append(None)

                if node.left:
                    st.append(node.left)
            else:
                node=st.pop()
                result.append(node.val)
        return result