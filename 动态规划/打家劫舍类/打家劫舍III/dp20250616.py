class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp=self.dfs(root)
        return max(dp)
    
    def dfs(self, root):
        """求解偷root和不偷root时的最大值"""
        if not root: # 如果root遇到了空节点
            return (0, 0)
        left_rob, left_not_rob = self.dfs(root.left)
        right_rob, right_not_rob = self.dfs(root.right)
        # 不偷
        not_rob = max(left_rob, left_not_rob)+max(right_rob, right_not_rob)
        # 偷
        rob = root.val+left_not_rob+right_not_rob
        return (rob, not_rob)