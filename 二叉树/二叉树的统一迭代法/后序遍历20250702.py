class Solution:
    def postorderTraversal(self, root):
        if root is None:
            return []
        result = []
        st = [root]
        while st:
            node = st.pop()
            if node is not None:
                st.append(node)
                st.append(None)
                if node.right:
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
            else:
                node = st.pop()
                result.append(node.val)
        return result