# 分析：
# 1. 后序数组为0，返回空节点
# 2. 后序数组最后一个元素作为节点元素
# 3. 寻找中序数组位置作为切割点
# 4. 切割中序数组（得到左中序数组和右中序数组）
# 5. 切割后序数组（得到左后序数组和右后序数组）--利用中序的切割结果来切割后序
# PS：一定要先切中序数组，再切后序数组
# 6. 递归处理左区间和右区间

# 时间复杂度：O(n^2)
# 1. 对于每次递归调用
# inorder.index(root_val)：查找当前根接待你在inorder数组中的位置，由于index是线性搜索，因此这个操作的时间复杂度为O(n)
# 切割inorder和postorder的时间复杂度为O(1)，仅仅是通过索引进行切分
# 2. 递归树的每一层都需要找到根节点在inorder数组中的位置，递归的层数是二叉树的高度，对于一个大小为n的二叉树来说，递归的最大深度为n

# 空间复杂度：O(n)
# 1. 递归调用的栈空间：最坏情况（链状）时递归栈的空间复杂度为O(n)
# 2. 切割数组时，inorder_left, inorder_right, postorder_left, postorder_right都会占用额外的空间，但是实际上这些只是对原数组的切片引用，不会拷贝数组内容，因此这部分的空间复杂度为O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int] 中序数组
        :type postorder: List[int] 后序数组
        :rtype: Optional[TreeNode] 
        """
        # 第一步：特殊情况讨论：树为空（递归终止条件）
        if not postorder:
            return None
        
        # 第二步：后序遍历的最后一个就是当前的中间节点
        root_val=postorder[-1] # 从postorder中取出最后一个元素
        root=TreeNode(root_val)

        # 第三步：找切割点
        separator_idx=inorder.index(root_val)

        # 第四步：切割inorder数组，得到inorder数组的左、右半边
        inorder_left=inorder[:separator_idx]
        inorder_right=inorder[separator_idx+1:]

        # 第五步：切割postorder数组，得到postorder数组的左，右半边
        # 利用inorder的切割结果来切割postorder
        postorder_left=postorder[:len(inorder_left)]
        postorder_right=postorder[len(inorder_left):len(postorder)-1]

        # 第六步：递归
        root.left=self.buildTree(inorder_left,postorder_left)
        root.right=self.buildTree(inorder_right,postorder_right)

        # 第七步：返回答案
        return root

        