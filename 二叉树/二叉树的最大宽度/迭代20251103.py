# 思路：求出每一层的宽度，然后求出最大值。
# 求每一层的宽度的时候，因为两个端点之间的null节点也需要计入宽度，因此可以对节点编号
# 一个编号为index的左子节点的编号记为2*index，右子节点的编号2*index+1
# 计算每层宽度的时候，用每层节点的最大编号减去最小编号再加1，即为宽度

# 遍历节点时，可以用BFS遍历每一层的节点，并求出最大值

# 时间复杂度：O(n)
# 空间复杂度：O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans, queue = 0, deque([(1, root)]) # label for each node(the label for root is 1)
        while queue: 
            mn, mx = inf, 0 # the minimal index for this level, the maximal index for this level
            for _ in range(len(queue)):
                ind, node = queue.popleft()
                if node.left:
                    queue.append([2*ind, node.left])
                if node.right:
                    queue.append([2*ind+1, node.right])
                # update the minimal index and maximal index in this level
                mn = min(ind, mn)
                mx = max(ind, mx)
            ans = max(ans, mx-mn+1) # update the largest width
        return ans