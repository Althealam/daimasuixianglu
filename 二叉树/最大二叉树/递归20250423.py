# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 时间复杂度：O(n)，其中n是数组nums的长度
# 空间复杂度：O(n)

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return None
        
        root=TreeNode(max(nums))
        mid=nums.index(root.val)

        root.left=self.constructMaximumBinaryTree(nums[:mid])
        root.right=self.constructMaximumBinaryTree(nums[mid+1:])
        return root
        