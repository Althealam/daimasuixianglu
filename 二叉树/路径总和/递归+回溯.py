# 方法：递归+回溯
# 思路：遍历路径，找到路径的和，判断是否等于targetSum
# 初始化count为targetSum，遇到一个节点就做减法，到叶子结点时判断是否count为0
# 这个题目前、中、后序遍历都可以用，因为我们不需要中间的
# 回溯是因为需要回退到上一个节点，然后判断另一条路径
# 1. 确定递归函数的参数和返回类型：二叉树的根节点，一个计数器（用来计算二叉树的一条边之和是否正好是目标和）
# 2. 确定终止条件：遍历到了叶子结点，count不为0，则表示没找到；遍历到了叶子结点，count为0，表示找到了目标和
# 3. 确定单层递归的逻辑
# 时间复杂度：O(n)
# 1. 树的遍历：递归函数 traversal 会遍历整棵树。对于每个非叶子节点，函数会递归遍历其左子树和右子树。
# 2. 单个结点的处理：在每次递归调用中，对每个节点只进行了常数次操作，例如减法和加法操作
# 空间复杂度：最坏情况下为O(n)，最好情况下为O(logn)
# 1. 递归栈空间：由于使用了递归，栈的深度取决于树的高度。对于一棵平衡二叉树，树的高度为 O(log N)；对于最坏情况下的退化树（链式结构），树的高度为 O(N)。
# 2. 额外空间：除了递归栈之外，该算法没有使用额外的空间（例如数组或哈希表）。递归过程中每次只在函数栈中存储局部变量 cur 和 count。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traversal(self,cur,count):
        if not cur.left and not cur.right and count==0: # 遇到叶子节点，并且计数为0
            return True
        if not cur.left and not cur.right: # 遇到叶子结点直接返回
            return False

        if cur.left:
            count-=cur.left.val
            if self.traversal(cur.left,count): # 递归，处理节点
                return True
            count+=cur.left.val # 回溯
        if cur.right:
            count-=cur.right.val
            if self.traversal(cur.right,count):
                return True
            count+=cur.right.val
        return False

             
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False
        return self.traversal(root,targetSum-root.val)
        