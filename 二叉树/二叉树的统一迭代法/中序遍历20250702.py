class Solution:
    def inorderTraversal(self, root):
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node!=None:
                if node.right:
                    st.append(node.right)
                st.append(node)
                st.append(None)
                if node.left:
                    st.append(node.left)
            else:
                node = st.pop()
                result.append(node.val)
        return result