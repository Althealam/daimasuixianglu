# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        st=[]
        result=[]
        if root:
            st.append(root)
        while st:
            node=st.pop()
            if node!=None:
                if node.right: # 右
                    st.append(node.right)
                st.append(node) # 中
                st.append(None) # 中节点访问过，但是还没有处理，加入空节点做标记
                if node.left: # 左
                    st.append(node.left)
            else: # 遇到空节点的时候，才将下一个节点放进结果集
                node=st.pop() # 重新取出栈中元素
                result.append(node.val) # 加入到结果集
        return result
                 