# 方法：迭代法
# 二叉搜索树：当进行中序遍历时，这个序列是有序的
# 代码误区：不能仅仅通过if root.val>root.left.val and root.val<root.right.val来进行判断，这只能保证根节点比左孩子大，比右孩子小，但是不能保证比左子树大，比右子树小
# 思路：已知二叉搜索树中序遍历时，数组是有序的，因此我们可以通过数组是否有序来判断是否是二叉搜索树

# 时间复杂度：该代码使用了中序遍历来检查二叉搜索树的有效性。中序遍历每个节点访问一次，因此时间复杂度为O(n)
# 空间复杂度：最坏情况下为O(n)，最好情况下为O(logn)
# 1. 栈的空间复杂度：栈的空间复杂度与二叉树的高度有关。
# （1）最坏情况：链表O(n)
# （2）最好情况：平衡二叉树O(logn)
# 2. 指针和变量的空间复杂度：O(1)

# 中序遍历的代码：
# class Solution(object):
#     def inorderTraversal(self, root):
#         stack = []
#         result = []
#         cur = root

#         while cur is not None or stack:
#             if cur is not None:
#                 stack.append(cur)
#                 cur = cur.left
#             else:
#                 cur = stack.pop()
#                 result.append(cur.val)  # 中序遍历记录当前节点值
#                 cur = cur.right

#         return result


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        stack=[]
        cur=root
        pre=None # 记录前一个节点
        # 使用迭代的中序遍历方式来遍历二叉树
        while cur is not None or len(stack)>0:
            # 1. 一直遍历左子树直到最左节点
            if cur is not None:
                stack.append(cur)
                cur=cur.left # 继续向左移动
            else:
                # 2. 左子树到底了，处理当前节点 
                cur=stack.pop() # 弹出栈顶元素，回到上一个节点
                # # 判断当前节点值是否小于等于前一个节点的值
                if pre is not None and cur.val<=pre.val:
                    return False # # 如果当前节点值不大于前一个节点值，则不是有效的BST
                # 更新前一个节点为当前节点
                pre=cur # 将 pre 指针更新为当前节点

                # 3. 转向右子树
                cur=cur.right # 准备遍历当前节点的右子树
        # 若遍历完整棵树且没有发现不符合条件的节点，则是有效的 BST
        return True