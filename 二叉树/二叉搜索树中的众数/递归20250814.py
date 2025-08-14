# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, res)
        hash_map = defaultdict(int)
        for num in res:
            if num not in hash_map:
                hash_map[num]=1
            else:
                hash_map[num]+=1
        max_cnt = max(hash_map.values())
        ans = []
        for num, cnt in hash_map.items():
            if cnt==max_cnt:
                ans.append(num)
        return ans
    
    def dfs(self, node, res):
        """中序遍历"""
        if not node:
            return None
        if node.left:
            self.dfs(node.left, res)
        res.append(node.val)
        if node.right:
            self.dfs(node.right, res)
        