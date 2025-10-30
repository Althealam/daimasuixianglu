# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorder(root, res)
        freq = {}
        for i in range(len(res)):
            if res[i] not in freq:
                freq[res[i]]=1
            else:
                freq[res[i]]+=1
        max_freq = max(freq.values())
        ans = []
        for num, cnt in freq.items():
            if cnt==max_freq:
                ans.append(num)
        return ans
    
    def inorder(self, root, res):
        if not root:
            return None
        if root.left:
            self.inorder(root.left, res)
        res.append(root.val)
        if root.right:
            self.inorder(root.right, res)
        