# 方法：递归法（版本二）
# 定义：最小深度是根节点到叶子结点的最小距离（如果不是到叶子结点的最小距离的话，可以直接修改求最大深度的代码）
# 需要判断某一子树为空的时候，这时候的二叉树的最小深度不可以是0
# 二叉树节点的深度：指的是从根节点到该节点到最长简单路径的条数
# 二叉树节点的高度：指的是从该节点到叶子结点的最长简单路径的条数
# 分析：递归三部曲
# 1. 确定递归函数的参数和返回值：参数为要传入的二叉树根节点，返回的是int类型的深度
# 2. 确定终止条件：种植条件是遇到空节点返回0，表示当前节点的高度为0
# 3. 确定单层递归的逻辑
# 后序遍历是用来求高度的。
# 时间复杂度：O(n)，最坏情况下，每个节点都会被访问一次
# 空间复杂度：最坏情况下为O(n)，最优情况下为O(logn)，空间复杂度取决于递归的深度
# 最坏情况下，树呈现链表状态，递归的深度达到树的最大高度，此时为O(n)
# 最好情况下，树是完全平衡的，递归深度为树的高度O(logn)
# 平衡二叉树：左右子树的高度差不超过1
# 为什么平衡二叉树的高度是logn：
# 假设树中有n个节点，在理想情况下平衡二叉树完全接近完全二叉树，在完全二叉树中，第i层最多有2^(i-1)个节点
# 其高度为h，则宗节点个数为2^h-1=n，可以知道h=log2(n+1)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def getDepth(self, node):
        """
        :type root: TreeNode
        :rtype: int
        """
        if node is None:
            return 0
        leftDepth=self.getDepth(node.left)
        rightDepth=self.getDepth(node.right)

        # 当一个左子树为空，右不为空，这时候并不是最低点
        if node.left is None and node.right is not None:
            return 1+rightDepth
        
        if node.right is None and node.left is not None:
            return 1+leftDepth
        
        result=1+min(leftDepth,rightDepth)
        return result
    
    def minDepth(self,root):
        return self.getDepth(root)