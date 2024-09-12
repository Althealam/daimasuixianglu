class Solution:
    def preorderTraversal(self,root:TreeNode)->list[int]:
        result=[]
        st=[]
        if root:
            st.append(root)
        while st:
            node=st.pop()
            if node!=None:
                if node.right: # 右孩子节点
                    st.append(node.right)
                if node.left: # 左孩子节点
                    st.append(node.left)
                st.append(node) # 中节点
                st.append(None)
            else:
                node=st.pop()
                result.append(node.val)
        return result