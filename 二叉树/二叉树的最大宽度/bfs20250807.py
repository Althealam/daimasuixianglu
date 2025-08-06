# 二叉树节点的定义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # 使用队列进行BFS，存储(节点, 节点位置)
        # 这里的位置采用完全二叉树的编号方式：根节点为1，左孩子为2*i，右孩子为2*i+1
        from collections import deque
        queue = deque()
        queue.append((root, 1))
        max_width = 0
        
        while queue:
            level_size = len(queue)
            # 记录当前层第一个和最后一个节点的位置
            first_pos = None
            last_pos = None
            
            for _ in range(level_size):
                node, pos = queue.popleft()
                
                # 记录当前层的第一个和最后一个节点位置
                if first_pos is None:
                    first_pos = pos
                last_pos = pos
                
                # 将左右孩子加入队列
                if node.left:
                    queue.append((node.left, 2 * pos))
                if node.right:
                    queue.append((node.right, 2 * pos + 1))
            
            # 当前层的宽度 = 最后一个节点位置 - 第一个节点位置 + 1
            current_width = last_pos - first_pos + 1
            max_width = max(max_width, current_width)
        
        return max_width

# 测试代码
def test():
    # 构建一个示例二叉树
    #       1
    #      / \
    #     3   2
    #    /     \
    #   5       9
    #  / \
    # 6   7
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.right.right = TreeNode(9)
    root.left.left.left = TreeNode(6)
    root.left.left.right = TreeNode(7)
    
    solution = Solution()
    print("二叉树的最大宽度为:", solution.widthOfBinaryTree(root))  # 预期输出: 4

test()
