# 方法：广度优先搜索
# 思路：广度优先搜索中的队列里存放的是当前层的所有节点。每次扩展下一层的时候，我们将当前队列中的全部节点拿出来进行扩展，这样能保证每次扩展完的时候队列里存放的是下一层的所有节点，即我们是一层一层的进行扩展，然后每一层利用maxVal来标记该层节点的最大值。
# 时间复杂度：O(n)，其中n为二叉树节点个数，每一个节点仅会进出队列一次
# 空间复杂度：O(n)，存储二叉树节点的空间开销
# 1. 队列q：这个队列用于存储每一层的节点，最坏的情况下队列中存储的节点数等于树的宽度
# 2. 临时列表tmp：在每次循环中被用来存储当前层的所有节点，最坏情况下也是O(n)
# 3. 结果列表ans：存储每一层的最大值

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        ans=[] # 初始化一个空列表ans，用于存储每一层的最大值
        q=[root] # 初始化一个队列q，并将根节点root加入队列（这个队列用于层次遍历二叉树）
        while q:
            maxVal=-inf # 帮助找到每一层的最大值
            tmp=q # 将当前层的节点存储到临时列表tmp中，以便在遍历这一层的节点时，队列q可以被用来存储下一层的节点。
            q=[] # 清空队列q，为存储下一层的节点做准备
            for node in tmp: # 遍历当前层的每一个节点
                maxVal=max(maxVal,node.val) # 更新当前层的最大值maxVal
                if node.left: # 如果节点有左子节点，将其加入到队列q
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(maxVal)
        return ans