# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 思路：用栈来中序遍历二叉树，然后每次遍历的时候都定义一个pre来保存上一个节点的值，判断pre和cur之间的节点大小情况

# 中序遍历-迭代法
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         if not root:
#             return []
#         stack=[]
#         result=[]
#         cur=root
#         while cur or stack:
#             # 迭代访问最底层的左节点
#             if cur:
#                 stack.append(cur)
#                 cur=cur.left
#             # 到达最左节点后处理栈顶节点
#             else:
#                 cur=stack.pop()
#                 result.append(cur.val)
#                 # 取栈顶元素右节点
#                 cur=cur.right
#         return result

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack=[]
        cur=root
        pre=None
        while stack or cur:
            if cur:
                stack.append(cur)
                cur=cur.left # 左 
            else:
                cur=stack.pop() # 中
                if pre and cur.val<=pre.val:
                    return False
                pre=cur
                cur=cur.right # 右
        return True
