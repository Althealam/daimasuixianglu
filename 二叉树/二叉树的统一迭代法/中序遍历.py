class Solution:
    def inorderTraversal(self,root:TreeNode)->list[int]:
        result=[]
        st=[]
        if root:
            st.append(root)
        while st:
            node=st.pop()
            if node!=None:
                if node.right: # 添加右节点（空节点不入栈）
                    st.append(node.right)
                
                st.append(node) # 添加中节点
                st.append(None) # 中节点访问过，但是还没有处理，加入空节点作为标记

                if node.left: # 添加左节点
                    st.append(node.left)
            else:
                node=st.pop() # 重新取出栈中元素
                result.append(node.val) # 加入到结果集
        return result