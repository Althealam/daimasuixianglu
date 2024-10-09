# 方法：广度优先搜索
# 思路：从根节点开始搜索，每一轮遍历同一层的全部节点，计算该层的节点数以及该层的节点值之和，然后计算该层的平均值
# 具体做法：
# 1. 初始时，将根节点加入队列；
# 2. 每一轮遍历时，将队列中的节点全部取出，计算这些节点的数量以及它们的节点值之和，并计算这些节点的平均值，然后将这些节点的全部非空子节点加入队列，重复上述操作直到队列为空，遍历结束
# 时间复杂度：O(n)，其中n是二叉树中的节点个数。广度优先搜素需要对每个节点访问一次，时间复杂度是O(n)，需要对二叉树的每一层计算平均值，时间复杂度为O(h)，其中h是二叉树的高度，任何情况下都是h<=n，因此总时间复杂度为O(n)
# 空间复杂度：O(n)，空间复杂度取决于队列开销，队列中的节点个数不会超过n

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def averageOfLevels(self, root):
        averages=list()
        queue=collections.deque([root])
        while queue:
            total=0
            size=len(queue)
            for _ in range(size):
                node=queue.popleft()
                total+=node.val
                left,right=node.left,node.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            averages.append(total/size)
        return averages
    
# 定义一个TreeNode类来构建二叉树
class TreeNode(object):
    # 初始化
    def __init__(self, val=0, left=None, right=None):
        self.val = val # 定义节点值
        self.left = left # 定义左子节点
        self.right = right # 定义右子节点

# 构建给定的二叉树
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# 创建Solution对象并计算平均值
solution = Solution()
averages = solution.averageOfLevels(root)
print(averages)