# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.vector = []
        self.inorder(root)
        cnt = defaultdict(int)
        for i in range(len(self.vector)):
            if self.vector[i] not in cnt:
                cnt[self.vector[i]]=1
            else:
                cnt[self.vector[i]]+=1
        max_freq = max(cnt.values())
        res = []
        for v in cnt.keys():
            if cnt[v]==max_freq:
                res.append(v)
        return res
    
    def inorder(self, root):
        if not root:
            return []
        def dfs(node):
            if node.left:
                dfs(node.left)
            self.vector.append(node.val)
            if node.right:
                dfs(node.right)
        dfs(root)


