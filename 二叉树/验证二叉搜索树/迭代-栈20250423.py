# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：用栈来中序遍历二叉树，然后每次遍历的时候都定义一个pre来保存上一个节点的值，判断pre和cur之间的节点大小情况

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack=[]
        cur=root
        pre=None # 前一个节点的值
        while stack or cur is not None:
            if cur is not None: # 非空
                stack.append(cur) 
                cur=cur.left # 左
            else: # 遇到空节点
                cur=stack.pop() # 中
                if pre is not None and pre.val>=cur.val: # 验证二叉搜索树
                    return False
                pre=cur # 保存上一个节点
                cur=cur.right # 递归下一个节点
        return True
                