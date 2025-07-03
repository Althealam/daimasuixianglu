max_depth_path = []

def get_depth_max(root):
    global max_depth_path 
    path = []

    def dfs(node):
        nonlocal path, max_depth_path
        if not node:
            return
        path.append(node.val)
        if node.left is None and node.right is None:
            if len(path) > len(max_depth_path):
                max_depth_path = path[:]  # 复制当前路径
        dfs(node.left)
        dfs(node.right)
        path.pop()  # 无论如何都 pop，保持路径正确

    dfs(root)
