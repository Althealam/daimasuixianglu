# 方法：广度优先搜索（BFS)
# 时间复杂度：
# 1. 遍历每一层：代码使用一个队列来逐层遍历二叉树，每一层都会被遍历一次
# 2. 每层节点的操作：对于每一层的每个节点，执行常数时间的操作（检查左右孩子节点并且添加到队列中）
# 3. 总节点数：假设二叉树有n个节点，那么时间复杂度就是O(n)，因为每个节点都会被访问一次
# 空间复杂度：
# 1. 队列空间：最坏的情况下，队列中可能包含树的最大宽度的所有节点
# 2. 结果列表：res包含了每一层的最后一个节点的值，最坏的情况下是O(h)，其中h为树的高度h

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        # 根节点入queue
        queue=[root]
        res=[] 
        # 初始化一个队列，将根节点加入队列
        # 初始化一个结果列表，用于存储每层的最后一个节点的值
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
        while queue:
            # 只需要对该层最后一个元素入列表
            res.append([node.val for node in queue][-1])
            # 存储当前层的孩子节点列表
            ll=[]
            # 对当前层的每个节点遍历
            for node in queue:
                # 如果左子节点存在，入队列
                if node.left:
                    ll.append(node.left)
                # 如果右子节点存在，入队列
                if node.right:
                    ll.append(node.right)
            # 后把queue更新成下一层的节点，继续遍历下一层
            queue=ll
        return res

# 测试代码
if __name__ == "__main__":
    # 创建一个示例二叉树
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    # 创建 Solution 对象
    solution = Solution()
    
    # 获取并打印二叉树的右视图
    right_view = solution.rightSideView(root)
    print("Right Side View:", right_view)