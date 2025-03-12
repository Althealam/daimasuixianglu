# 定义二叉树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 根据层序遍历数组构建二叉树
def buildTree(level_order):
    if not level_order:
        return None
    root = TreeNode(level_order[0])
    queue = [root]
    i = 1
    while queue and i < len(level_order):
        node = queue.pop(0)
        if level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1
        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1
    return root

# 计算树的高度
def treeHeight(root):
    if not root:
        return 0
    left_height = treeHeight(root.left)
    right_height = treeHeight(root.right)
    return max(left_height, right_height) + 1

# 以直观的方式打印二叉树
def printTree(root):
    if not root:
        return
    height = treeHeight(root)
    width = 2 ** height - 1
    result = [[' '] * width for _ in range(height)]

    def fill(node, row, left, right):
        if not node:
            return
        mid = (left + right) // 2
        result[row][mid] = str(node.val)
        fill(node.left, row + 1, left, mid - 1)
        fill(node.right, row + 1, mid + 1, right)

    fill(root, 0, 0, width - 1)
    for row in result:
        print(''.join(row))

# 主函数
def main():
    # 示例层序遍历数组，使用 None 表示空节点
    level_order = [1, 2, 3, 4, 5, None, 6]
    root = buildTree(level_order)
    printTree(root)

if __name__ == "__main__":
    main()