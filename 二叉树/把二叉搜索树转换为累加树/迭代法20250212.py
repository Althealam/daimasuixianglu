# 思路：迭代法
# 相当于得到一个二叉搜索树的有序数组（递减数组，因为遍历顺序是右中左）
# 然后将该有序数组进行累加操作，再覆盖掉原本的元素值

# 时间复杂度：O(n)
# 使用迭代的方式对二叉树进行遍历，在整个遍历过程中，每个节点都会被访问并且仅会被访问一次
# 当cur不为空的时候，会不断地将当前节点及其右子树的节点依次压入栈中
# 当cur为空的时候，会从栈中弹出节点进行处理，并转向左子树继续遍历

# 空间复杂度：O(h)
# 主要取决于栈stack的空间，而栈的空间大小与二叉树的高度有关

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traversal(self, root):
        stack=[] # 用来存储节点值
        cur=root
        while cur or stack:
            # 一直往右遍历，并且将节点依次放入到栈中
            if cur:
                stack.append(cur)
                cur=cur.right # 右
            # 右子树遍历完毕
            else:
                # 中的处理逻辑
                cur=stack.pop() 
                cur.val+=self.pre # 加上前一个节点的值
                self.pre=cur.val # 获得前一个节点的值

                cur=cur.left # 左
        
    def convertBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.pre=0 # 记录前一个节点的值
        self.traversal(root)
        return root
        