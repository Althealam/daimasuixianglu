# 方法：递归法
# 分析：将二叉搜索树看作是有序数组，然后更新有序数组即可
# 更新有序数组的方法为，保留数组中最大的元素，然后依次往前加
# 更新数组的时候，使用双指针即可，那么同理在二叉搜索树中使用双指针即可
# 我们需要从大到小遍历数组，因为这样我们就可以不用遍历整个数组找到最大值，因此我们在遍历二叉树时选择右中左的遍历顺序
# 利用双指针法来对节点值进行累加

# 时间复杂度：O(n)
# 1. 遍历每个树的节点：每个节点都会被访问一次
# 2. 每个节点的操作：对于每个节点，算法执行常数时间的操作（更新节点的值、修改pre）
# 空间复杂度：O(h)
# 1. 递归栈的空间：递归的深度由树的高度决定，因此递归调用栈的空间复杂度为O(h)，平衡树时为O(logn)，非平衡树时为O(n)
# 2. pre的空间：常数空间的变量，用来存储前一个节点的值，空间复杂度为O(1)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traversal(self,cur):
        if cur==None:
            return
        # 遍历右子树
        self.traversal(cur.right)
        # 遍历中间节点
        cur.val+=self.pre # 更新节点值
        self.pre=cur.val # 记录节点的值，准备下一步
        # 遍历左子树
        self.traversal(cur.left)
        return cur

    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.pre=0 # 记录前一个节点的数值
        self.traversal(root)
        return root




        