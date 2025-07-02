class Solution:
    def preorderTraversal(self, root):
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            # 不停的入栈直到遍历完所有的节点
            if node!=None:
                if node.right:
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
                st.append(node)
                st.append(None) # 用空指针标记节点
            # 此时已经将所有的节点入栈，因此可以弹出元素
            else:
                node = st.pop()
                result.append(node.val)
        return result