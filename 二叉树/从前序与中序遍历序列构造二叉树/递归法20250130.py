# 数组：
# 1. 如果数组大小为0，说明是空节点，直接返回空的二叉树
# 2. 如数组大小不为0，取前序数组的第一个元素作为节点元素，这是中节点
# 3. 找到中序数组节点值为中节点的值的位置，切割数组为中序左数组和中序右数组
# 4. 切割前序数组，切割成前序左数组和前序右数组
# 5. 递归处理左区间和右区间

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # 1. 判断数组长度是否为0
        if len(preorder)==0 or len(inorder)==0:
            return None
        
        # 2. 数组大小不为0，则找前序数组的第一个元素作为切割元素
        rootValue=preorder[0]
        root=TreeNode(rootValue)
        index=inorder.index(rootValue)

        # 3. 切割中序数组
        leftinorder=inorder[:index]
        rightinorder=inorder[index+1:]

        # 4. 切割前序数组
        leftpreorder=preorder[1:1+len(leftinorder)]
        rightpreorder=preorder[1+len(leftinorder):]

        # 5. 递归处理左区间和右区间
        root.left=self.buildTree(leftpreorder,leftinorder)
        root.right=self.buildTree(rightpreorder, rightinorder)
        return root