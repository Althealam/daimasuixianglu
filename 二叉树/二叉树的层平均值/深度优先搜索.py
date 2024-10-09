# 方法：深度优先搜索
# 思路：主要维护两个数组counts和sums，counts用于存储二叉树的每一层的节点数，sums用于存储二叉树的每一层的节点值之和
# 搜索过程中需要记录当前节点所在层，如果访问到的节点在第i层，则将counts[i]的值加1，并将该节点的值加到sums[i]
# 遍历结束后，第i层的平均值为sums[i]/counts[i]
# 时间复杂度：O(n)
# 深度优先搜索需要对每个节点访问一次，对于每个节点，维护两个数组的时间复杂度都是O(1)，因此深度优先搜索的时间复杂度为O(n)
# 空间复杂度：O(n)
# 空间复杂度取决于两个数组的大小和递归调用的层数，两个数组大小都等于二叉树的高度，递归调用的层数不会超过二叉树的高度。最坏的情况下，二叉树的高度等于节点个数

class Solution:
    def averageOfLevels(self, root):
#         3
#    / \
#   9  20
#     /  \
#    15   7
        def dfs(root, level):
            """
                root: 当前节点
                level: 当前节点的层级
            """
            # 如果当前节点root为空，返回（意味着我们到达了叶子结点的末尾）
            if not root:
                return
            # 检查当前节点的层级是否等于totals列表的长度，如果是，则代表我们到达了一个新的层级
            # totals记录的是每一层的节点值之和，因此len(totals)是遍历过的层数
            if level == len(totals):
                totals.append(root.val)
                counts.append(1)
            # 如果不是新的层级，即我们在同一层级内移动到另一个节点
            else:
                # 将当前节点的值累加到totals列表对应层级的综合中
                totals[level] += root.val
                # 增加counts列表对应层级的节点计数
                counts[level] += 1
            
            # 对当前节点的左子节点递归调用dfs函数
            dfs(root.left, level + 1)
            # 对当前节点的右子节点递归调用dfs函数
            dfs(root.right, level + 1)

        counts = []  # 用于存储每层的节点计数
        totals = []  # 用于存储每层的节点值之和
        dfs(root, 0) # 从根节点开始，层级为0，调用dfs函数
        
        # 计算每层的平均值
        return [total / count for total, count in zip(totals, counts)]


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