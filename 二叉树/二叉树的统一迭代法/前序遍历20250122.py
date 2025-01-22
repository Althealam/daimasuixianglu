# 思路：使用栈的时候，无法同时阶段访问节点（遍历节点）和处理节点（将节点放到结果集）不一致的情况
# 将访问的节点放入栈内，把要处理的节点也放入栈内但是要做标记（将要处理的节点入栈后，紧接着放一个空指针作为标记）

class TreeNode:
    def __init__(self,val=0,left=None, right=None):
        self.val=val
        self.right=right
        self.left=left

class Solution:
    def preorderTraversal(self, root):
        result=[]
        st=[]
        if root:
            st.append(root)
        while st:
            node=st.pop()
            if node!=None:
                if node.right: # 右
                    st.append(node.right)
                if node.left: # 左
                    st.append(node.left)
                st.append(node) # 中
                st.append(None) # 用空节点来标记一会要处理的节点
            else:
                node=st.pop()
                result.append(node.val)
        return result
    
   
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s=Solution()
print(s.preorderTraversal(root))

