# 分析：讨论当前节点抢还是不抢，如果抢了当前节点，两个孩子就不能动，如果没抢当前节点，就可以考虑抢左右孩子。

# 1. 确定递归函数的参数和返回值：要求一个节点偷与不偷的两个状态所得到的金钱
# 返回数组就是dp数组：下标为0表示不偷该节点所得到的最大金钱，下标为1记录偷该节点所得到的最大金钱
# 2. 终止条件：遍历过程中，遇到空节点的话就返回
# 3. 遍历顺序：后序遍历
# （1）递归左节点，得到左节点偷与不偷的金钱。
# （2）递归右节点，得到右节点偷与不偷的金钱。
# 4. 确定单层递归的逻辑：
# （1）偷当前节点，那么左右孩子不能偷
# （2）不偷当前节点，左右孩子可以偷
# 最后当前节点的状态就是{val2,val1}，即{不偷当前节点得到的最大金钱，偷当前节点得到的最大金钱}
# 头结点就是 取下标0 和 下标1的最大值就是偷得的最大金钱。

# 时间复杂度：O(n)（后序遍历节点）
# 空间复杂度：O(logn)
# 1. 递归栈深度：最好情况下为平衡二叉树，此时递归深度为logn；最坏情况下为单链表形状，递归深度为n
# 2. 局部变量：O(1)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # dp数组以及下标的含义：
        # 1. 下标为0记录“不偷该节点”所得到的最大金钱
        # 2. 下标为1记录“偷该节点”所得到的最大金钱
        dp=self.traversal(root)
        return max(dp)

    def traversal(self,node):
        # 递归终止条件，遇到空节点就不偷
        if not node:
            return (0,0)
        
        left=self.traversal(node.left)
        right=self.traversal(node.right)

        # 不偷当前节点，偷子节点
        val_0=max(left[0],left[1])+max(right[0],right[1])

        # 偷当前节点，不偷子节点
        val_1=node.val+left[0]+right[0]

        return (val_0,val_1)
        