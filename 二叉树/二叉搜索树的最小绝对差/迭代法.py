# 方法：迭代法
# 思路：在二叉搜索树上求最值/差值，可以想像成在一个有序数组上求最值/差值

# 时间复杂度：O(n)
# 代码中，通过一个while循环和stack栈结构来对树进行中序遍历。每个节点最多访问一次，执行一系列固定操作，因此总的时间复杂度为O(n)，其中n是树中节点的数量
# 空间复杂度：O(h)，其中h是树的高度
# 栈stack的空间消耗取决于树的高度
# （1）平衡二叉树为logn
# （2）链表为n


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self,root):
        stack=[]
        cur=root
        pre=None
        result=float('inf')

        while cur is not None or len(stack)>0:
            if cur is not None:
                stack.append(cur) # 将访问的节点放入栈内
                cur=cur.left # 左
            else:
                cur=stack.pop()
                if pre is not None: # 中
                    result=min(result,cur.val-pre.val)
                pre=cur
                cur=cur.right # 右
        return result