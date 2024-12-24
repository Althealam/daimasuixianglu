# 分析：
# 1. 前序数组为0，返回空节点
# 2. 前序数组的第一额元素作为节点元素
# 3. 寻找中序数组位置作为切割点
# 4. 切割中序数组
# 5. 切割前序数组
# 6. 递归处理左区间和右区间

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
        # 第一步：特殊情况讨论：树为空（递归终止条件）
        if not preorder:
            return None

        # 第二步：前序遍历的第一个就是当前的中间节点
        root_val=preorder[0]
        root=TreeNode(root_val)

        # 第三步：找切割点
        separator_idx=inorder.index(root_val)

        # 第四步：切割inorder数组，得到inorder数组的左、右半边
        inorder_left=inorder[:separator_idx]
        inorder_right=inorder[separator_idx+1:]

        # 第五步：切割preorder数组，得到preorder数组的左、右半边
        # 切割preorder数组这一块和切割postorder数组不一样，需要注意以下
        preorder_left=preorder[1:1+len(inorder_left)]
        preorder_right=preorder[1+len(inorder_left):]

        # 第六步：递归
        root.left=self.buildTree(preorder_left,inorder_left)
        root.right=self.buildTree(preorder_right,inorder_right)

        # 第七步：返回答案
        return root


        