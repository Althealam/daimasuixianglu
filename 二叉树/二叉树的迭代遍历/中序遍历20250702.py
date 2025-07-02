class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        stack = [] # 注意：中序遍历不能一开始就加入root，因为根节点需要在中间
        result = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            # 到达最左节点后处理栈顶节点
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right # 取右边的元素
        return result