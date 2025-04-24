# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n) 每个节点都会被访问并且仅被访问一次
# 空间复杂度：O(n) 
# 1. 最坏情况：二叉搜索树退化为链表 O(n)
# 2. 平均情况：平衡的二叉搜索树 O(logn)

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        prev=None
        stack=[]
        cur=root
        result=float('inf')
        while stack or cur:
            if cur:
                stack.append(cur) 
                cur=cur.left # 左
            else:
                cur=stack.pop() # 中
                if prev:
                    result=min(result, cur.val-prev.val)
                prev=cur
                cur=cur.right
        return result
