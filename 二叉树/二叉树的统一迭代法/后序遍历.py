class Solution:
    def postorderTraversal(self, root: TreeNode)->list(int):
        result=[]
        st=[]
        if root:
            st.append(root)
        while st:
            node=st.pop()
            if node!=None:
                st.append(node)
                st.append(None)

                if node.right:
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
            else:
                node=st.pop()
                result.append(node.val)
        return result