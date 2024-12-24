# 迭代法
# 思路：通过深度优先搜索（DFS）来遍历二叉树，并在遍历的过程中保存每条从根节点到叶子节点的路径。当找到一条路径的和等于 targetSum 时，将该路径保存到结果中

# 时间复杂度：
# 1. 树的遍历：每个节点都会被访问一次，并且在访问每个节点时会进行一些操作（比如，更新路径，检查是否为叶子节点，计算路径和等）。因此，遍历树的时间复杂度为 O(N)，其中 N 是树中节点的数量。
# 2. 路径和的计算：在每次找到叶子节点时，代码会计算路径上的节点和 sum(path)。每条路径的长度等于树的高度 H，因此计算路径和的时间复杂度是 O(H)。对于所有叶子节点来说，总的计算路径和的时间复杂度为 O(N * H)（假设有 O(N/2) 个叶子节点，每个叶子节点的路径长度为 O(H)）。
# 3. 总时间复杂度：由于树的高度 H 最多为 N，因此在最坏情况下，时间复杂度为 O(N * H)。对于平衡二叉树，H ≈ log N，此时时间复杂度为 O(N log N)。对于退化成链表的树，H ≈ N，时间复杂度为 O(N^2)。

# 空间复杂度：
# 1. 递归栈/迭代栈空间：使用了栈 stack 来模拟深度优先搜索。栈的最大深度等于树的高度 H，因此栈的空间复杂度为 O(H)。对于平衡树，H ≈ log N，空间复杂度为 O(log N)。对于退化成链表的树，H ≈ N，空间复杂度为 O(N)。
# 2. 路径存储空间：path 变量保存了当前从根节点到某个节点的路径，在最坏情况下，路径的长度为 H。每个节点都会有一个与之对应的 path，在最坏的情况下，树中的每个节点都在 stack 中保存一个路径副本，最坏情况下会保存所有叶子节点的路径，总共有 O(N) 条路径，每条路径的长度为 O(H)。因此，路径存储的空间复杂度是 O(N * H)。
# 3. 总空间复杂度：空间复杂度包括栈空间和路径存储空间，总体上为 O(N * H)。对于平衡二叉树，H ≈ log N，空间复杂度为 O(N log N)。对于退化成链表的树，H ≈ N，空间复杂度为 O(N^2)。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self,root,targetSum):
        if not root:
            return []
        stack=[(root,[root.val])]
        res=[]
        while stack:
            node,path=stack.pop()
            if not node.left and not node.right and sum(path)==targetSum:
                res.append(path)
            if node.right:
                stack.append((node.right,path+[node.right.val]))
            if node.left:
                stack.append((node.left,path+[node.left.val]))
        return res