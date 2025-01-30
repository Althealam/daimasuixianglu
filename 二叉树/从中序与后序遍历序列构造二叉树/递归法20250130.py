# 思路：
# 1. 如果数组大小为0，说明是空节点，直接返回空的二叉树
# 2. 如数组大小不为0，取后序数组的最后一个元素作为节点元素，这是中节点
# 3. 找到中序数组节点值为中节点的值的位置，切割数组为中序左数组和中序右数组
# 4. 切割后序数组，切割成后序左数组和后序右数组
# 5. 递归处理左区间和右区间

# 时间复杂度：O(n^2) 每次递归调用都要进行O(n)的查找和切割操作
# 1. 寻找根节点位置：O(n)
# 2. 数组切割：O(n)
# 3. 递归深度：O(logn)
# 空间复杂度：O(n)
# 1. 递归调用栈空间：最坏情况为O(n)，最好情况为O(logn)
# 2. 数组切割产生的额外空间：O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # 1. 判断数组的长度是否为0
        if len(inorder)==0 or len(postorder)==0:
            return None
        
        # 2. 找到后序数组的最后一个元素，就是当前的中节点
        rootValue=postorder[-1]
        root=TreeNode(rootValue)

        # 3. 找到中序数组节点值为中节点的位置，也就是切割点
        # index=0
        # for index in range(len(inorder)):
        #     if inorder[index]==rootValue:
        #         break
        index=inorder.index(rootValue)

        # 切割中序数组
        leftinorder=inorder[:index]
        rightinorder=inorder[index+1:]
        
        # 4. 切割后序数组
        leftpostorder=postorder[:len(leftinorder)]
        rightpostorder=postorder[len(leftinorder):len(postorder)-1]

        # 5. 递归遍历左右中序和后序数组
        root.left=self.buildTree(leftinorder,leftpostorder)
        root.right=self.buildTree(rightinorder, rightpostorder)

        return root        