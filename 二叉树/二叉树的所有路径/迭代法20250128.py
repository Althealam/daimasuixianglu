# 迭代法
# 时间复杂度：通过模拟DFS（深度优先搜索）遍历二叉树的每一个节点，因此是O(n)
# 每个节点都会被访问一次，并且在访问每个节点的时候执行的操作的时间复杂度都是常数级别的
# 空间复杂度：由stack和path_st占用的空间决定
# 1. 最坏情况：二叉树是链，递归深度达到最大，此时stack和path_n都需要存储n个节点的路径信息，最坏情况下时间复杂度是O(n^2)
# 2. 平均情况：平衡二叉树，高度是h=log2n，stack和path_st最多存储logn的元素，假设路径数是O(n)，平均路径长度是O(log2n)，因此存储路径所需要的空间是O(nlog2n)

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
        if not root:
            return []
        stack=[root] # 用来遍历节点
        path_st=[str(root.val)] # 记录本条路线
        result=[] # 用来保存所有二叉树从根节点到叶子节点的遍历路径

        while stack:
            cur=stack.pop()
            path=path_st.pop() # 模拟了递归调用的回溯过程
            # 如果当前节点是叶子节点，则添加路径到结果中
            if not cur.left and not cur.right:
                result.append(path)
            # 处理子节点
            if cur.right:
                # 如果当前节点cur有右子节点，将右子节点加入到stack中，并在当前路径path的基础上，拼接上右子节点的值，形成新的路径并加入到path_st中
                stack.append(cur.right)
                path_st.append(path+'->'+str(cur.right.val))
            if cur.left:
                # 如果当前节点cur有左子节点，将左子节点加入到stack中，并在当前路径path的基础上，拼接上左子节点的值，加入到path_st中
                stack.append(cur.left)
                path_st.append(path+'->'+str(cur.left.val))
        return result
        