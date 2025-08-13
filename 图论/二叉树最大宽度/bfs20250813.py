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
        res = 1 # 最大宽度，初始化为根节点层的宽度
        arr = [[root, 1]] # 存储当前层的节点以及编号，初始化为根节点（节点+编号1）
        while arr: # 当当前层有节点时，继续遍历
            tmp = [] # 存储下一层的节点以及编号
            for node, index in arr: # 遍历当前层的所有节点，收集下一层节点
                if node.left: # 左节点存在时，记录其编号
                    tmp.append([node.left, index*2])
                if node.right: # 右节点存在时，记录其编号
                    tmp.append([node.right, index*2+1])
            # 计算当前层的宽度：最右节点编号-最左节点编号+1
            res = max(res, arr[-1][1]-arr[0][1]+1)
            # 将下一层节点转换为当前层，继续循环
            arr = tmp
        return res

        