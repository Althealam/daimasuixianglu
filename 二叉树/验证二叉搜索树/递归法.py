# 方法：递归法（利用中序递增性质，转换为数组）
# 二叉搜索树：当进行中序遍历时，这个序列是有序的
# 代码误区：不能仅仅通过if root.val>root.left.val and root.val<root.right.val来进行判断，这只能保证根节点比左孩子大，比右孩子小，但是不能保证比左子树大，比右子树小
# 思路：已知二叉搜索树中序遍历时，数组是有序的，因此我们可以通过数组是否有序来判断是否是二叉搜索树

# 时间复杂度：O(n)
# isValidBST 函数首先调用了 traversal 函数，对二叉树进行中序遍历。
# 1. 中序遍历的时间复杂度为O(n)，因为每个节点都会被访问一次
# 2. isValidBST中的for循环需要遍历生成vec数组，此时的时间复杂度也为O(n)
# 综上，总的时间复杂度为O(n)+O(n)=O(n)

# 空间复杂度：O(n)
# 1. traversal函数是递归调用的，最坏情况下需要O(h)的空间来保存递归栈，h是二叉树的高度
# （1）平衡二叉树：h=logn
# （2）非平衡二叉树（链表）：h=n
# 2. 存储中序遍历的数组vec：vec数组保存了所有节点的值，因此为O(n)
# 综上，空间复杂度为O(h)+O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        self.vec=[] # 定义存储二叉树的中序遍历的数组

    def traversal(self,root):
        if root is None:
            return
        self.traversal(root.left) # 左
        self.vec.append(root.val) # 中
        self.traversal(root.right) # 右
    
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        self.vec=[] # 清空数组
        self.traversal(root) # 求数组
        for i in range(1,len(self.vec)):
            # 注意要小于等于，搜索树内不能有相同的元素
            if self.vec[i]<=self.vec[i-1]:
                return False 
        return True       