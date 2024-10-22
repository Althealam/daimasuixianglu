# 方法：递归法+回溯（精简版）
# 思路：找树最下角的值，指的是在树的最后一行（最底层）找到最左边的值。深度最大的叶子节点一定是最后一行
# 使用哪个遍序方式都可以，因为没有遍历中
# 分析：
# 1. 确定递归函数的参数和返回值：参数必须有要遍历的树的根节点，还有一个int型变量来记录最大深度
# 2. 确定终止条件：当遇到叶子结点的时候，就需要统计最大深度了
# 3. 确定单层递归的逻辑：在找最大深度的时候，递归过程中依然要使用回溯
# 时间复杂度：O(n)，每个节点都会被访问一次
# 空间复杂度：空间复杂度取决于递归调用栈的深度。O(h)，其中h为树的高度。最坏情况下为O(n)（不平衡树），最好情况下为O(logn)（平衡树）
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.max_depth=float('-inf')
        self.result=None
        self.traversal(root,0)
        return self.result

    # 寻找最大深度
    def traversal(self,node,depth):
        if not node.left and not node.right: # 到达叶子结点
            if depth>self.max_depth: # 寻找最大深度
                self.max_depth=depth
                self.result=node.val
            return

        # 未到达叶子结点
        if node.left:
            self.traversal(node.left,depth+1)
        if node.right:
            self.traversal(node.right,depth+1)
