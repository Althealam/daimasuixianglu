# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = []
        prev = None
        cur = root
        res = []
        max_count, count = 0, 0
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if prev and prev.val==cur.val:
                    count+=1
                elif prev and prev.val!=cur.val:
                    count=1
                else:
                    count=1
                if count==max_count:
                    res.append(cur.val)
                if count>max_count:
                    max_count = count
                    res = [cur.val]
                prev = cur
                cur = cur.right
        return res