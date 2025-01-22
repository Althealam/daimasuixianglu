class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def postorderTraversal(self, root):
        result=[]
        st=[]
        if root:
            st.append(root)
        while st:
            node=st.pop()
            if node!=None:
                st.append(node) #中
                st.append(None)

                if node.right:
                    st.append(node.right)
                if node.left:
                    st.append(node.left)
            else: # 只有遇到空节点的时候，才将下一个节点放进结果集
                node=st.pop()
                result.append(node.val)
        return result