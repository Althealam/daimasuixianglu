# 方法：迭代法
# 路径：根节点到叶子结点的路径
# 分析：使用前序遍历，这样才会出现父结点指向孩子节点，这样才能输出从根节点到叶子结点的路径
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        stack,path_st,result=[root],[str(root.val)],[]

        while stack:
            cur=stack.pop()
            path=path_st.pop()
            # 如果当前节点为叶子结点，添加路径到结果中
            if not (cur.left or cur.right):
                result.append(path)
            if cur.right:
                stack.append(cur.right)
                path_st.append(path+'->'+str(cur.right.val))
            if cur.left:
                stack.append(cur.left)
                path_st.append(path+'->'+str(cur.left.val))
        return result