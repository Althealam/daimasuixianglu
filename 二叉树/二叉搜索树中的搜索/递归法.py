# 方法：递归法
# 二叉搜索树的定义：根节点比左子树大，根节点比右子树小（它的左、右子树也为二叉搜索树）
# 1. 确定递归函数的参数和返回值：递归函数的参数传入的就是根节点和要搜索的数值，返回的就是以这个搜索数值所在的节点。
# 2. 确定终止条件：如果root为空，或者找到这个数值了，就返回root节点。
# 3. 确定单层递归的逻辑：如果root->val > val，搜索左子树，如果root->val < val，就搜索右子树，最后如果都没有搜索到，就返回NULL。
# 二叉搜索树不需要考虑遍历顺序

# 时间复杂度：
# 1. 平衡二叉搜索树：
# 在平衡的 BST 中，树的高度为 O(log n)，其中 n 是树中节点的数量。每次递归调用都排除了一半的节点，因此时间复杂度为 O(log n)。
# 2. 非平衡二叉搜索树：
# 在最坏的情况下，树退化成链表（例如插入顺序导致的极端不平衡），高度为 O(n)，因此最坏情况下时间复杂度为 O(n)。

# 空间复杂度：
# 1. 平衡二叉搜索树：
# 对于平衡的 BST，递归深度为 O(log n)，因此空间复杂度为 O(log n)。
# 2. 非平衡二叉搜索树：
# 在最坏的情况下，树的高度为 O(n)，递归深度可能达到 n，因此最坏情况下的空间复杂度为 O(n)。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        if root==None or root.val==val:
            return root
        result=TreeNode() 
        if val<root.val:
            result=self.searchBST(root.left,val) # 有返回值，因此需要一个变量来接住返回值
        if val>root.val:
            result=self.searchBST(root.right,val)
        return result