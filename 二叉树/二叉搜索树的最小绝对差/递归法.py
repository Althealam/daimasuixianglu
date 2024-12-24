# 方法：递归法（利用中序递增，结合数组）
# 思路：在二叉搜索树上求最值/差值，可以想像成在一个有序数组上求最值/差值

# 时间复杂度：
# 1. 中序遍历的时间复杂度：函数 traversal 对树进行了中序遍历。时间复杂度为O(n)，因为每个节点访问一次。
# 2. 计算最小差值的时间复杂度：遍历完成后，代码会对self.vec中的元素逐对比较差值，这里的for循环执行n-1次，时间复杂度也为O(n)
# 因此，总的时间复杂度为O(n)+O(n)=O(n)

# 空间复杂度：
# 1. 递归栈的空间复杂度：traversal使用递归来遍历树，递归栈的最大深度为树的高度。
# （1）平衡二叉树：O(logn)
# （2）链表：O(n)
# 2. 存储有序数组的空间复杂度：self.vec存储了树中所有节点的值，因此空间复杂度为O(n)
# 因此，总的时间复杂度为O(h)+O(n)约等于O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.vec=[]

    def traversal(self,root):
        if root is None:
            return
        self.traversal(root.left) 
        self.vec.append(root.val) # 将二叉搜索树转换为有序数组
        self.traversal(root.right)

    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.vec=[]
        self.traversal(root)
        if len(self.vec)<2:
            return 0
        result=float('inf')
        for i in range(1,len(self.vec)):
            # 统计有序数组的最小差值
            result=min(result,self.vec[i]-self.vec[i-1])
        return result
        