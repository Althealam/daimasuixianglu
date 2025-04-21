# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 分析：类比层序遍历的方法
# 时间复杂度：O(n)
# 1. 节点遍历：使用DFS对二叉树的每个节点进行访问，每个节点都会出栈和入栈一次，节点的遍历操作时间复杂度为O(n)
# 空间复杂度：O(n)（主要由栈空间决定）
# 1. 栈空间：最坏情况下，二叉树退化为链表，栈的深度达到O(n)，因此需要依次将每个节点入栈，所以栈所占用的空间为O(n)
# 2. 结果空间：result存储从根节点到叶子节点的所有路径，最坏情况下，二叉树的每个节点都是叶子节点，结果列表中会存储O(n)条路径，每条路径的长度最多为O(n)


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack=[root]
        path_st=[str(root.val)]
        result=[]
        while stack:
            cur=stack.pop()
            path=path_st.pop()
            # 当前节点为叶子节点
            if cur.left is None and cur.right is None:
                result.append(path)
            # 加入右孩子节点
            if cur.right:
                stack.append(cur.right)
                path_st.append(path+'->'+str(cur.right.val))
            # 加入左孩子节点
            if cur.left:
                stack.append(cur.left)
                path_st.append(path+'->'+str(cur.left.val))
        return result